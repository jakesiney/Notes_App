from flask import Blueprint, render_template

# Create a Blueprint object named 'main'. The first argument is the Blueprint's name, which is used by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint's resources.

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('base.html')
