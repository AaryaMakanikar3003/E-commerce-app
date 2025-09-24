# 🛒 E-commerce App (Flask + MongoDB)

A role-based **E-commerce web application** built with **Flask** and **MongoDB**, featuring authentication, authorization, and CRUD operations for products, customers, and orders.  

The system supports two types of users:
- **Admin** → Can add, edit, delete, and view all products, customers, and orders.
- **Customer** → Can register, log in, browse products, and place/view their own orders.

---

## 🚀 Features

- 🔑 **Role-Based Authentication**
  - Admin and Customer roles with separate permissions.
  - Only Admin can edit or delete data.
  - Customers can only view and place their own orders.

- 👥 **User Management**
  - Register and login system with roles stored in MongoDB.
  - Session-based authentication.

- 📦 **Product Management**
  - Admin: Add, update, delete, and view products.
  - Customer: View product catalog.

- 🧾 **Order Management**
  - Customers: Place and view their own orders.
  - Admin: View and manage all orders.

- 🎨 **Frontend**
  - HTML templates using Jinja2.
  - CSS for styling (inside `static/`).

---

## 📂 Project Structure

ecommerce_app/
│
├── app.py # Main Flask app entry point
├── config.py # Configurations (DB URI, secret keys, etc.)
├── requirements.txt # Python dependencies
├── README.md # Project description, setup, usage
│
├── controllers/ # Route handlers
│ ├── init.py
│ ├── auth.py
│ ├── products.py
│ ├── orders.py
│ └── customers.py
│
├── models/ # Only product model exists
│ ├── init.py
│ └── products.py
│
├── templates/ # All HTML files
│ ├── boilerplate/ # Common HTML parts
│ │ ├── navbar.html
│ │ └── footer.html
│ ├── product_add.html
│ ├── product_edit.html
│ ├── product_list.html
│ ├── order_add.html
│ ├── order_list.html
│ ├── customer_profile.html
│ ├── customer_list.html
│ ├── login.html
│ └── register.html
│
├── static/ # Static files
│ └── style.css # Only CSS file directly here
│
└── datasets/ # Initial data and seed files
├── users_init.py
├── users_data.py
├── products_init.py
├── products_data.py
├── customers_init.py
└── customers_data.py


---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Frontend**: HTML, CSS (Jinja2 templates)
- **Auth**: Flask sessions (role-based access control)

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/E-commerce-app.git
   cd E-commerce-app
