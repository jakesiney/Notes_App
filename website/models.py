from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # The second argument is the default value of the column. In this case, we're using SQLAlchemy's func.now() function to set the default value to the current time.
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # The third argument is a ForeignKey, which is a column that references the primary key of another table. In this case, we're referencing the id column of the User table.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# Create a relationship between the User and the Note models. The first argument is the model to map to, and the second argument is the name of the field that will be used to access the relationship from the User model.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
