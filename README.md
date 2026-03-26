# 🚀 Streamlit SaaS App with Stripe Payments

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-1.29-orange?logo=streamlit)](https://streamlit.io/)  
[![Stripe](https://img.shields.io/badge/stripe-payments-6772e5?logo=stripe)](https://stripe.com/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple **SaaS application** built with **Streamlit**, **SQLite**, **SQLAlchemy**, and **Stripe**.  
Users can register, log in, upgrade to a premium plan, and visualize sales data through an interactive dashboard.

---

## 🌟 Features

- **User Authentication**
  - Register and login with username & password
  - Secure password hashing with bcrypt
- **Subscription Management**
  - Free & PRO plans
  - Upgrade to PRO using Stripe Checkout
  - Automatic plan update after payment success
- **Interactive Dashboard**
  - Shows user info, plan, and account status
- **Data Analytics**
  - Sample sales data table and line chart
  - Premium analytics for PRO users
- **Modern UI**
  - Streamlit cards & sidebar navigation
  - Responsive and clean design

---

## 🛠️ Tech Stack

- **Backend & Database:** SQLite + SQLAlchemy  
- **Authentication:** Passlib (bcrypt)  
- **Payments:** Stripe API  
- **Frontend:** Streamlit  
- **Data Visualization:** Pandas + Streamlit charts  

---

## ⚙️ Installation

1. **Clone the repository**

bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo


**Install dependencies**

pip install -r requirements.txt

**Configure environment variables in app.py:**

STRIPE_SECRET_KEY = "your_stripe_secret_key"
STRIPE_PRICE_ID = "your_stripe_price_id"
BASE_URL = "http://localhost:8501"

**Run the app**

streamlit run app.py

**📦 Optional: Docker Deployment**

FROM python:3.11-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

**Build and run:**

docker build -t saas-app .
docker run -p 8501:8501 saas-app
