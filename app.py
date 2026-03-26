import stripe
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from passlib.hash import bcrypt
import pandas as pd

# =========================
# CONFIG
# =========================
STRIPE_SECRET_KEY = "sk_test_xxx"
STRIPE_PRICE_ID = "price_xxx"
BASE_URL = "http://localhost:8501"

DATABASE_URL = "sqlite:///saas.db"

stripe.api_key = STRIPE_SECRET_KEY

# =========================
# DATABASE
# =========================
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    plan = Column(String, default="free")

Base.metadata.create_all(bind=engine)

# =========================
# SESSION
# =========================
if "user" not in st.session_state:
    st.session_state.user = None

# =========================
# UI CONFIG
# =========================
st.set_page_config(page_title="SaaS App", layout="wide")

st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}
.card {
    padding:20px;
    border-radius:12px;
    background:white;
    box-shadow:0 4px 14px rgba(0,0,0,0.08);
}
.sidebar .sidebar-content {
    background:#111827;
}
</style>
""", unsafe_allow_html=True)

# =========================
# AUTH FUNCTIONS
# =========================
def register(username, password):
    hashed = bcrypt.hash(password)
    user = User(username=username, password=hashed)
    db.add(user)
    db.commit()

def login(username, password):
    user = db.query(User).filter_by(username=username).first()
    if user and bcrypt.verify(password, user.password):
        return user
    return None

# =========================
# STRIPE
# =========================
def create_checkout_session(username):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": STRIPE_PRICE_ID,
            "quantity": 1,
        }],
        mode="subscription",
        success_url=f"{BASE_URL}?success=true",
        cancel_url=f"{BASE_URL}?canceled=true",
        metadata={"user": username}
    )
    return session.url

# =========================
# LOGIN / REGISTER
# =========================
if not st.session_state.user:

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.title("🔐 Login")

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
        st.title("📝 Register")

        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            register(new_user, new_pass)
            st.success("User created")

# =========================
# MAIN APP
# =========================
else:
    user = db.query(User).filter_by(username=st.session_state.user).first()

    # SIDEBAR
    st.sidebar.title("🚀 SaaS App")
    st.sidebar.write(f"👤 {user.username}")
    st.sidebar.write(f"Plan: {user.plan}")

    menu = st.sidebar.radio("Navigation", ["Dashboard", "Premium", "Data"])

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()

    # =====================
    # DASHBOARD
    # =====================
    if menu == "Dashboard":
        st.title("📊 Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f'<div class="card">User<br><h2>{user.username}</h2></div>', unsafe_allow_html=True)

        with col2:
            st.markdown(f'<div class="card">Plan<br><h2>{user.plan}</h2></div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="card">Status<br><h2>Active</h2></div>', unsafe_allow_html=True)

    # =====================
    # PREMIUM FEATURE
    # =====================
    elif menu == "Premium":
        st.title("💎 Premium Features")

        if user.plan == "free":
            st.warning("Upgrade to PRO to access this feature")

            if st.button("Upgrade to PRO"):
                url = create_checkout_session(user.username)
                st.markdown(f"[Go to Payment]({url})")

        else:
            st.success("Welcome PRO user 🎉")

            st.markdown('<div class="card">🔥 Premium Analytics Enabled</div>', unsafe_allow_html=True)

    # =====================
    # DATA PAGE
    # =====================
    elif menu == "Data":
        st.title("📂 Data Page")

        data = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "Sales": [100, 150, 80, 200, 170]
        })

        st.dataframe(data, use_container_width=True)

        st.line_chart(data.set_index("Day"))

    # =====================
    # STRIPE RETURN
    # =====================
    params = st.query_params

    if "success" in params:
        user.plan = "pro"
        db.commit()
        st.success("Payment successful! You are now PRO 🎉")

    if "canceled" in params:
        st.error("Payment canceled")
