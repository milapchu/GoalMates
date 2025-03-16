from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .db import db  # Now import db from website.db
from .models import Category

category = Blueprint('category', __name__)

# Display all categories to the user (GET method)
@category.route('/category')
@login_required
def show_categories():
    return render_template("category.html")


# @category.route('/select_category', methods=['GET', 'POST'])
# def select_category():
#     if request.method == 'POST':
#         category = request.form.get('category')
#         # You can use the category value here if needed
#         # For now, just redirect to 'a.html'
#         return redirect(url_for('categorydetails.html'))
#     return render_template('category.html')

@category.route('/categorydetails')
def categorydetails():
    return render_template('categorydetails.html') 