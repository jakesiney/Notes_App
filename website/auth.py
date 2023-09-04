from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


# Create a Blueprint object named 'auth'. The first argument is the Blueprint's name, which is used by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint's resources.
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again.', category='error')

    return render_template("login.html", bool=True)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Get the data from the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Get the first user with the email
        existing_user = User.query.filter_by(email=email).first()
        # Check if the user already exists

        if existing_user:
            flash(
                'Email already exists, please use login or use a different email', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Add user to the database
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.index'))

    return render_template("sign_up.html")
