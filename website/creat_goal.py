from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website import db 
from .models import Task, Group 
import datetime

@app.route('/create_goal', methods=['GET', 'POST'])
@login_required
def create_goal():
    if request.method == 'POST':
        goal_name = request.form.get('goal_name')
        description = request.form.get('description')
        start_date = request.form.get('start_date')  # Expected in "YYYY-MM-DD" format
        end_date = request.form.get('end_date')  # Expected in "YYYY-MM-DD" format

        # Convert start_date and end_date string to datetime objects
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD for both start and end dates.', category='error')
            return redirect(url_for('create_goal'))  # Redirect to the same page for the user to try again

        # Check if goal name already exists for the user (optional)
        existing_goal = Goal.query.filter_by(goal_name=goal_name, user_id=current_user.id).first()

        if existing_goal:
            flash('You already have a goal with this name', category='error')
        else:
            # Create a new goal
            new_goal = Goal(
                goal_name=goal_name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                user_id=current_user.id
            )
            db.session.add(new_goal)
            db.session.commit()

            flash('Goal created successfully!', category='success')
            return redirect(url_for('views.goals'))  # Redirect to a view that shows user's goals
    
    return render_template("create_goal.html", user=current_user)
