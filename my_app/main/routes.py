# from datetime import datetime

from flask import Blueprint, render_template, request, make_response, redirect, url_for, session
from flask_login import current_user

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', defaults={'name': 'traveler'})
@main_bp.route('/<name>')
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username
    return render_template('index.html', title="Home page",
                           name=name)
