from flask import render_template, current_app, Blueprint, request, redirect, url_for, flash, json

orders_bp = Blueprint('orders', __name__)

# View all orders
@orders_bp.route('/orders')
def orders():
    mongo = current_app.mongo
    all_orders = list(mongo.db.orders.find())
    return render_template('orders.html', orders=all_orders)

# View details of a single order
@orders_bp.route('/orders/<order_id>')
def order_details(order_id):
    mongo = current_app.mongo
    order = mongo.db.orders.find_one({'order_id': order_id})
    if not order:
        return "Order not found, 404!"
    return render_template('order_details.html', order=order)

# Add a new order
# @orders_bp.route('/orders/add', methods=['POST', 'GET'])
# def order_add():
#     mongo = current_app.mongo
#     if request.method == 'POST':
#         # Get products list from form
#         products = []
#         product_ids = request.form.getlist('product_id')
#         quantities = request.form.getlist('quantity')
#         prices = request.form.getlist('price')

#         total_amount = 0
#         for i in range(len(product_ids)):
#             total = float(quantities[i]) * float(prices[i])
#             total_amount += total
#             products.append({
#                 "product_id": product_ids[i],
#                 "name": request.form.getlist('name')[i],
#                 "quantity": int(quantities[i]),
#                 "price": float(prices[i]),
#                 "total": total
#             })

#         new_order = {
#             "order_id": request.form.get("order_id"),
#             "customer_id": request.form.get("customer_id"),
#             "customer_name": request.form.get("customer_name"),
#             "products": products,
#             "total_amount": total_amount,
#             "order_date": request.form.get("order_date"),
#             "status": request.form.get("status"),
#             "shipping_address": {
#                 "street": request.form.get("street"),
#                 "city": request.form.get("city"),
#                 "state": request.form.get("state"),
#                 "zip": request.form.get("zip")
#             },
#             "payment_method": request.form.get("payment_method")
#         }

#         mongo.db.orders.insert_one(new_order)
#         flash('New order added!')
#         return redirect(url_for('orders.orders'))
#     else:
#         product_id = request.args.get('product_id')
#         product_name = request.args.get('product_name')
#         price = request.args.get('price')
#         quantity = int(request.args.get('quantity', 1))
        
#         prefill_products = []
#         total_amount = 0
#         if product_id and product_name and price:
#             price = float(price)
#             total_amount = price * quantity
#             prefill_products = [{
#                 "product_id": product_id,
#                 "name": product_name,
#                 "quantity": 1,
#                 "price": float(price),
#                 "total": float(total_amount)
#             }]
#         return render_template('order_add.html', prefill_products=prefill_products, prefill_total=total_amount)

@orders_bp.route('/orders/add', methods=['POST', 'GET'])
def order_add():
    mongo = current_app.mongo

    if request.method == 'POST':
        # Get products list from form (JSON string or list)
        products_json = request.form.get("products")
        try:
            products = json.loads(products_json) if products_json else []
        except Exception as e:
            flash("Invalid products JSON format!")
            return redirect(url_for('orders.order_add'))

        # Calculate total_amount automatically from products
        total_amount = sum([float(p['total']) for p in products])

        new_order = {
            "order_id": request.form.get("order_id"),
            "customer_id": request.form.get("customer_id"),
            "customer_name": request.form.get("customer_name"),
            "products": products,
            "total_amount": total_amount,
            "order_date": request.form.get("order_date"),
            "status": request.form.get("status"),
            "shipping_address": {
                "street": request.form.get("street"),
                "city": request.form.get("city"),
                "state": request.form.get("state"),
                "zip": request.form.get("zip")
            },
            "payment_method": request.form.get("payment_method")
        }

        mongo.db.orders.insert_one(new_order)
        flash('New order added!')
        return redirect(url_for('orders.orders'))

    else:
        # Prefill product info if coming from "Buy Now"
        prefilled_products = request.args.get('products')
        prefilled_total = 0
        products_list = []

        if prefilled_products:
            try:
                products_list = json.loads(prefilled_products)
                prefilled_total = sum([float(p['total']) for p in products_list])
            except Exception:
                products_list = []
                prefilled_total = 0

        return render_template(
            'order_add.html',
            prefilled_products=json.dumps(products_list),
            prefilled_total=prefilled_total
        )


# Edit an order
@orders_bp.route('/orders/<order_id>/edit', methods=['POST', 'GET'])
def order_edit(order_id):
    mongo = current_app.mongo
    order = mongo.db.orders.find_one({'order_id': order_id})
    if request.method == 'POST':
        # For simplicity, updating only main details, not products list dynamically
        try:
            products = json.loads(request.form.get("products"))
        except Exception as e:
            flash("Invalid JSON in products field. Please check formatting.")
            return redirect(url_for('orders.order_edit', order_id=order_id))
        updated_data = {
            "customer_id": request.form.get("customer_id"),
            "customer_name": request.form.get("customer_name"),
            "status": request.form.get("status"),
            "payment_method": request.form.get("payment_method"),
            "total_amount":request.form.get('total_amount'),
            "order_date": request.form.get("order_date"),
            "products": products,
            "shipping_address": {
                "street": request.form.get("street"),
                "city": request.form.get("city"),
                "state": request.form.get("state"),
                "zip": request.form.get("zip")
            }
        }
        mongo.db.orders.update_one({'order_id': order_id}, {'$set': updated_data})
        flash('Order updated!')
        return redirect(url_for('orders.order_details', order_id=order_id))
    else:
        return render_template('order_edit.html', order=order)

# Delete an order
@orders_bp.route('/orders/<order_id>/del', methods=['POST'])
def order_delete(order_id):
    mongo = current_app.mongo
    result = mongo.db.orders.delete_one({'order_id': order_id})
    if result.deleted_count > 0:
        flash('Order deleted successfully!')
    else:
        flash('No order deleted!')
    return redirect(url_for('orders.orders'))
