from flask import render_template, current_app, Blueprint, request, redirect, url_for, flash

products_bp=Blueprint('products', __name__)

@products_bp.route('/products')
def products():
    mongo=current_app.mongo
    products_collection=mongo.db.products
    
    all_products=list(products_collection.find())
    return render_template('products.html', products=all_products)

@products_bp.route('/products/<product_id>')
def product_details(product_id):
    mongo=current_app.mongo
    product=mongo.db.products.find_one({'product_id':product_id})
    if not product:
        return "Product not found, 404!"
    return render_template('product_details.html', product=product)

@products_bp.route('/products/<product_id>/edit', methods=['POST', 'GET'])
def product_edit(product_id):
    mongo=current_app.mongo
    product_to_be_edited=mongo.db.products.find_one({'product_id':product_id})
    if request.method=='POST':
        updated_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description'),
            'images': [request.form.get('images')] if request.form.get('images') else [],
            'price': request.form.get('price'),
            'compare_at_price': request.form.get('compare_at_price'),
            'cost_per_item': request.form.get('cost_per_item'),
            'weight': request.form.get('weight'),
            'inventory_quantity': request.form.get('inventory_quantity'),
            'status': request.form.get('status'),
            'dimensions': {
                "length": float(request.form.get("length")) if request.form.get("length") else 0.0,
                "width": float(request.form.get("width")) if request.form.get("width") else 0.0,
                "height": float(request.form.get("height")) if request.form.get("height") else 0.0
            }
        }
        mongo.db.products.update_one({'product_id':product_id}, {'$set': updated_data})
        return redirect(url_for('products.product_details', product_id=product_id))
    else:
        return render_template('product_edit.html', product_to_be_edited=product_to_be_edited)
    
@products_bp.route('/products/<product_id>/del', methods=['POST'])
def product_delete(product_id):
    mongo=current_app.mongo
    result=mongo.db.products.delete_one({'product_id':product_id})
    if result.deleted_count>0:
        flash('Product deleted successfully!')
    else:
        flash('No product deleted!')
    return redirect(url_for('products.products'))
        
@products_bp.route('/products/add', methods=['POST', 'GET'])
def product_add():
    mongo=current_app.mongo
    if request.method=='POST':
        image_url = request.form.get("image") or ""
        new_product={
            "product_id": request.form.get("product_id"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "images": [image_url],
            "price": request.form.get("price"),
            "compare_at_price": request.form.get("compare_at_price"),
            "cost_per_item": request.form.get("cost_per_item"),
            "weight": request.form.get("weight"),
            "inventory_quantity": request.form.get("inventory_quantity"),
            "status": request.form.get("status"),
            "dimensions": {
                "length": float(request.form.get("length")) if request.form.get("length") else 0.0,
                "width": float(request.form.get("width")) if request.form.get("width") else 0.0,
                "height": float(request.form.get("height")) if request.form.get("height") else 0.0
            }
        }
        mongo.db.products.insert_one(new_product)
        flash('New product added!')
        return redirect(url_for('products.products'))
    else:
        return render_template('product_add.html')
