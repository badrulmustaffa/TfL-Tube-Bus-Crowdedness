from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from my_app import db, photos
from my_app.community.forms import ProfileForm
from my_app.models import Profile, User

forum_bp = Blueprint('forum_bp', __name__, url_prefix='/forum')


@forum_bp.route('/', defaults={'name': 'traveler'})
@login_required
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username
    return render_template('index.html',
                           title='Forum',
                           message='This page is still empty',
                           name=name)
