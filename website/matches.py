import datetime
from flask import Blueprint, render_template
from .models import User
from itertools import combinations
from difflib import SequenceMatcher
from flask_login import login_required, current_user

match_bp = Blueprint('match', __name__)

users = [
    {"name": "Mila", "age": 20, "category": "academic", "detail_goal": "WAM 90", "from": "16/03/2025", "to": "19/07/2027"},
    {"name": "May", "age": 22, "category": "academic", "detail_goal": "WAM 85", "from": "01/04/2025", "to": "20/12/2027"},
    {"name": "Alex", "age": 25, "category": "fitness", "detail_goal": "Lose 10kg", "from": "10/01/2025", "to": "10/07/2025"},
    {"name": "Clariya", "age": 21, "category": "academic", "detail_goal": "WAM 89", "from": "20/02/2025", "to": "15/09/2027"},
    {"name": "Celine", "age": 21, "category": "academic", "detail_goal": "WAM 88", "from": "20/03/2025", "to": "15/08/2027"},
    {"name": "Nara", "age": 21, "category": "fitness", "detail_goal": "Gained 5kg", "from": "18/07/2025", "to": "15/09/2027"},
    {"name": "Meo", "age": 19, "category": "fitness", "detail_goal": "Gained 3kg", "from": "15/06/2025", "to": "15/07/2027"},
    {"name": "Himi", "age": 18, "category": "hobby", "detail_goal": "Success Violin", "from": "16/05/2025", "to": "13/02/2027"},
    {"name": "Serry", "age": 20, "category": "hobby", "detail_goal": "Fluent Violin", "from": "16/04/2025", "to": "13/04/2027"}
]

def similar_goal(goal1, goal2, threshold=0.5):
    """Check if two goals are similar based on string matching."""
    similarity = SequenceMatcher(None, goal1.lower(), goal2.lower()).ratio()
    return similarity >= threshold  # If similarity score is 50% or higher, consider it a match

def match_users(users):
    matched_groups = []
    used_users = set() 

    # Sort users by category, age, and start date
    users_sorted = sorted(users, key=lambda x: (x["category"], x["age"], x["from"], x["to"]))

    for user1, user2 in combinations(users_sorted, 2):  # Compare pairs
        if user1["name"] in used_users or user2["name"] in used_users:
            continue  # Skip already matched users

        # Convert date strings to datetime objects
        start_date_1 = datetime.datetime.strptime(user1["from"], "%d/%m/%Y")
        start_date_2 = datetime.datetime.strptime(user2["from"], "%d/%m/%Y")
        end_date_1 = datetime.datetime.strptime(user1["to"], "%d/%m/%Y")
        end_date_2 = datetime.datetime.strptime(user2["to"], "%d/%m/%Y")

        # Check matching criteria
        if (
            user1["category"] == user2["category"] and
            abs(user1["age"] - user2["age"]) <= 3 and  # Age difference ≤ 3 years
            similar_goal(user1["detail_goal"], user2["detail_goal"]) and  # Check goal similarity
            abs((start_date_1 - start_date_2).days) <= 60 and  # Start date within 2 months
            abs((end_date_1 - end_date_2).days) <= 180  # End date within 6 months
        ):
            matched_groups.append([user1, user2])
            used_users.update([user1["name"], user2["name"]])

    return matched_groups

@match_bp.route('/match')
@login_required  # Requires user to be logged in
def match(users):
    matched_pairs = match_users(users)  # Replace with actual user data from the database
    return render_template("matches.html", matched_pairs=matched_pairs, user=current_user)
