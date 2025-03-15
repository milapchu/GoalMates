from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Enum
from datetime import datetime


# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # data = db.Column(db.String(10000))
#     # date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     first_name = db.Column(db.String(150))
#     category = db.relationship('Category')

# from . import db
# from flask_login import UserMixin
# from sqlalchemy.sql import func

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100))  # Add this field to store the selected category
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # Define the relationship to User model
    user = db.relationship('User', backref='categories')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
    # Define the relationship to Category model
    category = db.relationship('Category')

