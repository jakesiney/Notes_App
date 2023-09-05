from flask import Blueprint, render_template
from flask_login import login_required, current_user


# Create a Blueprint object named 'main'. The first argument is the Blueprint's name, which is used by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint's resources.

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    # render_template() is a Flask function that takes a template file name as an argument. Flask will look for the template file in the templates folder. Flask will then render the template file as HTML and return it to the client.
    return render_template('home.html', user=current_user)
