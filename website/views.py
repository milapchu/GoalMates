from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/category', methods=['GET', 'POST'])
@login_required
def category():
    return render_template("category.html", user=current_user)


@views.route('/match', methods=['GET', 'POST'])
@login_required
def match():
    return render_template("matches.html", user=current_user)