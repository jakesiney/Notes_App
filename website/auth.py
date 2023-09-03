from flask import Blueprint, render_template

# Create a Blueprint object named 'main'. The first argument is the Blueprint's name, which is used by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint's resources.

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
