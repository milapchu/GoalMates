from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .db import db  # Now import db from website.db
from .models import Category, User

category = Blueprint('category', __name__)

