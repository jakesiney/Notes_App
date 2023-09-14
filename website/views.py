from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note
from .import db
import json

# Create a Blueprint object named 'main'. The first argument is the Blueprint's name, which is used by Flask's routing mechanism. The second argument, __name__, is the Blueprint's import name, which Flask uses to locate the Blueprint's resources.

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        # Get the data from the form
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            # Create a new note object

        # Add the new note to the database
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')
    # render_template() is a Flask function that takes a template file name as an argument. Flask will look for the template file in the templates folder. Flask will then render the template file as HTML and return it to the client.
    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Get the id of the note to be deleted
    note = json.loads(request.data)
    noteId = note['noteId']
    # Find the note in the database
    note = Note.query.get(noteId)
    # If the note exists, delete it
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
