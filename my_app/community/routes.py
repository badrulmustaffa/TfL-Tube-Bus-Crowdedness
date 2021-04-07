from flask import Blueprint, render_template
from flask_login import login_required, current_user

community_bp = Blueprint('community_bp', __name__, url_prefix='/community')


@community_bp.route('/', defaults={'name': 'traveler'})
@login_required
def index(name):
    if not current_user.is_anonymous:
        name = current_user.firstname
    return render_template('index.html',
                           title='Community page',
                           message='This page is still empty',
                           name=name)
