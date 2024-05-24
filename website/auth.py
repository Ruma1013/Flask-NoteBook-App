from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')  # Correct the decorator to route
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

