from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Association Table for Many-to-Many relationship between Category & User
user_category = db.Table(
    'user_category',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100))
    users = db.relationship('User', secondary=user_category, back_populates='categories')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    categories = db.relationship('Category', secondary=user_category, back_populates='users')
