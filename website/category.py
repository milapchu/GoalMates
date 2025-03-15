from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .db import db  # Now import db from website.db
from .models import Category, User

category = Blueprint('category', __name__)

# Display all categories to the user (GET method)
@category.route('/category')
@login_required
def show_categories():
    return render_template("category.html")