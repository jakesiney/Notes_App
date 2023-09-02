from flask import Blueprint, render_template

# Create a Blueprint object named 'main'. The first argument is the Blueprint's name, which is used by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint's resources.

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"