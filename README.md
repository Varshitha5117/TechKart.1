# 🛒 TechKart - E-commerce Web Application

TechKart is a modern full-stack e-commerce web application designed to provide users with a seamless online shopping experience. It allows users to browse, search, and purchase a variety of products — including both new and refurbished electronics. Built using Django for the backend and HTML/CSS/JS for the frontend, TechKart integrates core functionalities like authentication, cart management, checkout system, and more.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

##  Features

- User Authentication (Sign Up / Login / Logout)
- Product Listings (Normal and Refurbished)
- Detailed Product Pages
- Add to Cart & Cart Management
- Checkout Process
- Responsive Design
- Admin Dashboard to Manage Products
- Secure backend with Django ORM and CSRF protection

---

##  Tech Stack

**Frontend:**
- HTML5
- CSS3
- JavaScript
- Bootstrap (for responsiveness)

**Backend:**
- Python
- Django Framework

**Database:**
- SQLite (can be upgraded to PostgreSQL)

**Other Tools:**
- Django Admin
- Django Messages Framework
- Git & GitHub

---


---

## ⚙️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/Varshitha5117/TechKart.1.git
cd TechKart.1


2.Create a Virtual Environment 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Install Dependencies
pip install -r requirements.txt

4.Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Server
python manage.py runserver

6. Visit on Browser
http://127.0.0.1:8000/



---


----
## Future Enhancements
Razorpay/Stripe payment gateway integration

Product review and rating system

Email notifications for orders

Wishlist functionality

Search autocomplete suggestions

API support with Django REST Framework




## License
This project is open-source and available under the MIT License.

