# Cartify - E-commerce Web Application

Cartify is a simple e-commerce web application built using **Flask** and **MongoDB**. It allows users to browse products, add them to a cart, and place orders. Admin users can manage products and view all orders.

---

## Features

### For Users
- View all products with images and details
- See product dimensions, weight, and inventory
- Place orders using "Buy Now" button
- Order history view
- Search products

### For Admin
- Add, edit, and delete products
- Manage orders
- View detailed order information

---

## Technologies Used
- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Frontend:** HTML, Bootstrap 5, Jinja2 templates
- **Other:** JavaScript for interactivity

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd <your-project-folder>

Cartify/
│
├── app.py                       # Main Flask app: initializes Flask, MongoDB, registers blueprints
│
├── controllers/                 # Controllers (Blueprints)
│   ├── products.py              # Product-related routes & logic
│   ├── orders.py                # Order-related routes & logic
│   ├── customers.py             # Customer-related routes & logic
│   └── auth.py                  # Authentication routes & logic
│
├── templates/                   # HTML templates
│   ├── boilerplate/             # Partial templates
│   │   ├── navbar.html          # Navbar
│   │   └── footer.html          # Footer
│   │
│   ├── products.html
│   ├── product_details.html
│   ├── product_add.html
│   ├── product_edit.html
│   ├── orders.html
│   ├── order_details.html
│   ├── order_add.html
│   ├── order_edit.html
│   ├── customers.html
│   └── customer_details.html
│
├── static/                      # Static assets
│   └── css/
│       └── style.css            # Custom styles (navbar colors, text size, etc.)
│
├── datasets/                    # Scripts to prefill DB with initial data
│   ├── product_data.py
│   ├── product_init.py
│   ├── order_data.py
│   ├── order_init.py
│   ├── customer_data.py
│   └── customer_init.py
│
├── requirements.txt             # Python dependencies
└── README.md                    # Project description & instructions

