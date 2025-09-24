# Sample users for auth (admin and customers)

sample_users = [
    {
        "user_id": "USER001",
        "username": "admin1",
        "email": "admin@example.com",
        "password": "admin123",  # we will hash it later in real app
        "role": "admin"          # can add/edit/delete products/orders
    },
    {
        "user_id": "USER002",
        "username": "john_doe",
        "email": "john@example.com",
        "password": "customer123",
        "role": "customer"       # can only place orders / view products
    },
    {
        "user_id": "USER003",
        "username": "jane_doe",
        "email": "jane@example.com",
        "password": "customer123",
        "role": "customer"
    }
]
