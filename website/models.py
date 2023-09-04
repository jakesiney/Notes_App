from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 10000 is the max length of the note
    data = db.Column(db.String(10000))
    # timezone=True is used to store the time in UTC format
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # default=func.now() is used to set the default value of the date column to the current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user_id is the foreign key that connects the Note table to the User table


class User(db.Model, UserMixin):
    # primary_key=True means that the id column is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # unique=True means that the email column can only contain unique values
    email = db.Column(db.String(150), unique=True)
    # 150 is the max length of the first name
    first_name = db.Column(db.String(150))
    # 150 is the max length of the password
    password = db.Column(db.String(150))
    # notes is a relationship between the User table and the Note table
    notes = db.relationship('Note')
