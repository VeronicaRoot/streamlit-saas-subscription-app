🚀 Streamlit SaaS App with Stripe Payments
This is a simple SaaS application built with Streamlit, SQLite, SQLAlchemy, Passlib, and Stripe for subscription management. Users can register, log in, upgrade to a premium plan, and visualize data through a dashboard.
💡 Features
User Authentication
Register and log in with username and password
Passwords hashed securely with bcrypt
Subscription Management
Free and PRO plans
Upgrade to PRO using Stripe Checkout
Automatic plan update after successful payment
Dashboard
Shows user info, plan status, and account activity
Data Visualization
Simple sales data displayed as a table and line chart
Premium users have access to enhanced analytics
Streamlit UI
Modern, responsive cards for information
Sidebar navigation and user session management
⚙️ Tech Stack
Backend / Database: SQLite + SQLAlchemy
Authentication: Passlib (bcrypt)
Payments: Stripe API
Frontend / UI: Streamlit
Data Visualization: Pandas + Streamlit charts

🛠️ Installation
Clone the repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Install dependencies
pip install -r requirements.txt
Set up environment variables
STRIPE_SECRET_KEY = "your_stripe_secret_key"
STRIPE_PRICE_ID = "your_stripe_price_id"
BASE_URL = "http://localhost:8501"
Run the app
streamlit run app.py
🧾 Usage
Open the app in your browser at http://localhost:8501
Register a new user or log in
Access the Dashboard to see account info
Go to Premium to upgrade to PRO plan via Stripe
Visit Data to see sample analytics
💳 Stripe Integration
Uses Stripe Checkout for subscriptions
Metadata stores the username for linking payment to account
Plan status is updated automatically on success
🔐 Security
Passwords are hashed using bcrypt
Sessions are managed with st.session_state
Stripe keys should never be exposed publicly
