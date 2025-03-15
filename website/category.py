from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .db import db  # Now import db from website.db
from .models import Category, User

category = Blueprint('category', __name__)

# Display all categories to the user (GET method)
@category.route('/categories')
@login_required
def show_categories():
    categories = Category.query.all()
    return render_template("category.html", categories=categories, user=current_user, )

# Add a user to a category (POST method via AJAX)
@category.route('/join-category/<int:category_id>', methods=['POST'])
@login_required
def join_category(category_id):
    category = Category.query.get(category_id)

    if not category:
        return jsonify({"error": "Category not found"}), 404

    # Check if user is already a part of the category
    if category in current_user.categories:
        return jsonify({"message": "You are already part of this category"}), 400

    # Add the category to the user’s categories
    current_user.categories.append(category)
    db.session.commit()

    return jsonify({"message": f"Joined category {category.cat_name} successfully!"}), 200
