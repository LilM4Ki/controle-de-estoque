from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

home_route = Blueprint('home', __name__)
@home_route.route('/')
@login_required
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return render_template('index.html', user = current_user)