from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from my_app import db, photos
from my_app.community.forms import ProfileForm
from my_app.models import User, History

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', defaults={'name': 'traveler'})
@main_bp.route('/<name>')
def index(name):
    return redirect('/navigation_dash/')


@main_bp.route('/save/<mean>/<start>/<end>', methods=['GET', 'POST'])
def save_journey(mean, start, end):
    if not current_user.is_anonymous:
        journey = History(mean=mean, start=start, end=end,
                          user_id=current_user.id)
        db.session.add(journey)
        db.session.commit()
    return redirect(url_for('main_bp.index'))
