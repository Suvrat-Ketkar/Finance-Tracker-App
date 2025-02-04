from flask import render_template, Blueprint, session
from app.authentication.auth import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    username = session.get('username', 'User')  # Retrieve username from session
    return render_template('HomePage.html', username=username)
