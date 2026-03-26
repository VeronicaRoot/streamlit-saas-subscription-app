# 🚀 SaaS Subscription App with Streamlit, Stripe & Authentication

A complete **SaaS starter template** built with **Streamlit**, featuring:

* 🔐 User Authentication (Login/Register)
* 💳 Subscription Payments via Stripe
* 📊 Dashboard UI
* 🗄️ SQLite Database (easy to upgrade)
* 👤 User-based access control
* 🚀 Ready for deployment

---

## 🧰 Tech Stack

* Python
* Streamlit
* Stripe API
* SQLAlchemy (ORM)
* Passlib (Password Hashing)

---

## 📸 Features

* Authentication system (secure password hashing)
* Stripe Checkout integration
* Subscription plans (Free / Pro)
* Session management
* Simple dashboard
* Easy to extend into production SaaS

---

## ⚙️ Installation

```bash
pip install streamlit stripe sqlalchemy passlib
```

---

## 🔑 Stripe Setup

1. Create account: https://dashboard.stripe.com/register
2. Get your API key:

   * `STRIPE_SECRET_KEY`
3. Create a product + price (monthly subscription)
4. Replace in code:

   ```python
   STRIPE_SECRET = "your_secret_key"
   PRICE_ID = "your_price_id"
   ```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
saas-streamlit-app/
│── app.py
│── saas.db
│── README.md
```

---

## 🧠 How It Works

1. User registers or logs in
2. Free users can upgrade to PRO
3. Stripe Checkout handles payment
4. After success → user upgraded to PRO
5. UI updates based on subscription

---

## ⚠️ Production Notes

This is a **starter template**. For real production:

* Use webhooks (Stripe events)
* Move secrets to environment variables
* Use PostgreSQL instead of SQLite
* Add backend (FastAPI)
* Enable HTTPS

---

## 🔮 Future Improvements

* Webhook integration
* Subscription cancel/upgrade
* Admin dashboard
* Multi-tenant architecture
* AI integration

---

## 📜 License

MIT License

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
