# from datetime import datetime

from flask import Blueprint, render_template, request, make_response, redirect, \
    url_for, session, flash
from flask_login import current_user

from my_app.main.forms import NavigationForm
from my_app.main.functions import RenderMap

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/', defaults={'name': 'traveler'})
@main_bp.route('/<name>')
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username
    return render_template('index.html', title="Home page",
                           name=name)


@main_bp.route('/navigation', methods=['GET', 'POST'])
def navigation():
    form = NavigationForm()
    if request.method == 'POST':
        map = RenderMap(form.mean.data)
        start = form.start.data
        end = form.end.data

        flash("Well Done")
        return redirect(url_for('main_bp.index'))
    return render_template('navigation.html', form=form)
