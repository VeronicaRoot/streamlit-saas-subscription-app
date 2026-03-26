import streamlit as st
import stripe
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from passlib.hash import bcrypt

# =====================
# CONFIG
# =====================
STRIPE_SECRET = "sk_test_xxx"
PRICE_ID = "price_xxx"

stripe.api_key = STRIPE_SECRET

engine = create_engine("sqlite:///saas.db")
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()
Base = declarative_base()

# =====================
# MODELS
# =====================
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    plan = Column(String, default="free")

Base.metadata.create_all(bind=engine)

# =====================
# SESSION
# =====================
if "user" not in st.session_state:
    st.session_state.user = None

# =====================
# AUTH FUNCTIONS
# =====================
def register(username, password):
    user = User(username=username, password=bcrypt.hash(password))
    db.add(user)
    db.commit()

def login(username, password):
    user = db.query(User).filter_by(username=username).first()
    if user and bcrypt.verify(password, user.password):
        return user
    return None

# =====================
# STRIPE CHECKOUT
# =====================
def create_checkout_session(username):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": PRICE_ID,
            "quantity": 1,
        }],
        mode="subscription",
        success_url="http://localhost:8501/?success=true",
        cancel_url="http://localhost:8501/?canceled=true",
        metadata={"user": username}
    )
    return session.url

# =====================
# LOGIN / REGISTER UI
# =====================
if not st.session_state.user:

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.title("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login(username, password)
            if user:
                st.session_state.user = user.username
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        st.title("Register")

        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            register(new_user, new_pass)
            st.success("User created successfully")

# =====================
# MAIN APP
# =====================
else:
    user = db.query(User).filter_by(username=st.session_state.user).first()

    st.sidebar.write(f"👤 {user.username}")
    st.sidebar.write(f"Plan: {user.plan}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    st.title("Subscription Dashboard")

    if user.plan == "free":
        st.warning("You are on Free Plan")

        if st.button("Upgrade to PRO"):
            checkout_url = create_checkout_session(user.username)
            st.markdown(f"[Proceed to Payment]({checkout_url})")

    else:
        st.success("You are a PRO user 🎉")

    # Handle redirect params (demo only)
    params = st.query_params

    if "success" in params:
        user.plan = "pro"
        db.commit()
        st.success("Payment successful! You are now PRO 🎉")

    if "canceled" in params:
        st.error("Payment canceled")
