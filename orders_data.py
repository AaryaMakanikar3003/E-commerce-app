# orders_data.py
sample_orders = [
    {
        "order_id": "ORD001",
        "customer_id": "CUST001",
        "customer_name": "John Doe",
        "products": [
            {"product_id": "JEANS002", "name": "Slim Fit Denim Jeans", "quantity": 2, "price": 49.99, "total": 99.98},
            {"product_id": "SHIRT001", "name": "Casual Shirt", "quantity": 1, "price": 29.99, "total": 29.99}
        ],
        "total_amount": 129.97,
        "order_date": "2025-09-20",
        "status": "Pending",
        "shipping_address": {"street": "123 Main St", "city": "Pune", "state": "MH", "zip": "411001"},
        "payment_method": "COD"
    },
    {
        "order_id": "ORD002",
        "customer_id": "CUST002",
        "customer_name": "Alice Smith",
        "products": [
            {"product_id": "DRESS001", "name": "Floral Dress", "quantity": 1, "price": 59.99, "total": 59.99}
        ],
        "total_amount": 59.99,
        "order_date": "2025-09-19",
        "status": "Shipped",
        "shipping_address": {"street": "456 Park Ave", "city": "Mumbai", "state": "MH", "zip": "400001"},
        "payment_method": "Card"
    },
    {
        "order_id": "ORD003",
        "customer_id": "CUST003",
        "customer_name": "Bob Johnson",
        "products": [
            {"product_id": "SHOES001", "name": "Running Shoes", "quantity": 1, "price": 79.99, "total": 79.99},
            {"product_id": "SOCKS001", "name": "Ankle Socks", "quantity": 3, "price": 5.99, "total": 17.97}
        ],
        "total_amount": 97.96,
        "order_date": "2025-09-18",
        "status": "Delivered",
        "shipping_address": {"street": "789 Lake Rd", "city": "Bangalore", "state": "KA", "zip": "560001"},
        "payment_method": "Card"
    },
    {
        "order_id": "ORD004",
        "customer_id": "CUST001",
        "customer_name": "John Doe",
        "products": [
            {"product_id": "HAT001", "name": "Baseball Cap", "quantity": 2, "price": 19.99, "total": 39.98}
        ],
        "total_amount": 39.98,
        "order_date": "2025-09-20",
        "status": "Cancelled",
        "shipping_address": {"street": "123 Main St", "city": "Pune", "state": "MH", "zip": "411001"},
        "payment_method": "COD"
    }
]
