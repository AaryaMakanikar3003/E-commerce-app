from flask import render_template, current_app, Blueprint, request, redirect, url_for, flash

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers')
def customers():
    mongo = current_app.mongo
    all_customers = list(mongo.db.customers.find())
    return render_template('customers.html', customers=all_customers)

@customers_bp.route('/customers/<customer_id>')
def customer_details(customer_id):
    mongo = current_app.mongo
    customer = mongo.db.customers.find_one({'customer_id': customer_id})
    if not customer:
        return "Customer not found, 404!"
    return render_template('customer_details.html', customer=customer)

@customers_bp.route('/customers/add', methods=['POST', 'GET'])
def customer_add():
    mongo = current_app.mongo
    if request.method == 'POST':
        new_customer = {
            "customer_id": request.form.get("customer_id"),
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "address": {
                "street": request.form.get("street"),
                "city": request.form.get("city"),
                "state": request.form.get("state"),
                "zip": request.form.get("zip")
            },
            "status": request.form.get("status")
        }
        mongo.db.customers.insert_one(new_customer)
        flash('New customer added!')
        return redirect(url_for('customers.customers'))
    else:
        return render_template('customer_add.html')

@customers_bp.route('/customers/<customer_id>/edit', methods=['POST', 'GET'])
def customer_edit(customer_id):
    mongo = current_app.mongo
    customer = mongo.db.customers.find_one({'customer_id': customer_id})
    if request.method == 'POST':
        updated_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "address": {
                "street": request.form.get("street"),
                "city": request.form.get("city"),
                "state": request.form.get("state"),
                "zip": request.form.get("zip")
            },
            "status": request.form.get("status")
        }
        mongo.db.customers.update_one({'customer_id': customer_id}, {'$set': updated_data})
        flash('Customer updated!')
        return redirect(url_for('customers.customer_details', customer_id=customer_id))
    else:
        return render_template('customer_edit.html', customer=customer)

@customers_bp.route('/customers/<customer_id>/del', methods=['POST'])
def customer_delete(customer_id):
    mongo = current_app.mongo
    result = mongo.db.customers.delete_one({'customer_id': customer_id})
    if result.deleted_count > 0:
        flash('Customer deleted successfully!')
    else:
        flash('No customer deleted!')
    return redirect(url_for('customers.customers'))
