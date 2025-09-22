from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mongo = current_app.mongo
        username = request.form.get('username')
        password = request.form.get('password')

        user = mongo.db.users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):  # plain text for now; later use hash
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['role'] = user['role']
            flash(f"Logged in as {user['username']}")
            return redirect(url_for('products.products'))
        else:
            flash('Invalid credentials!')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

# REGISTER ROUTE
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    mongo = current_app.mongo
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'customer')  # allow role selection (optional)

        # check if user already exists
        if mongo.db.users.find_one({'email': email}):
            flash('Email already registered!', 'warning')
            return redirect(url_for('auth.register'))

        hashed_pw = generate_password_hash(password)
        mongo.db.users.insert_one({
            'username': username,
            'email': email,
            'password': hashed_pw,
            'role': role
        })
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


# Logout route
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect(url_for('auth.login'))
