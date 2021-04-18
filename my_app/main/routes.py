# from datetime import datetime
import flask
from flask import Blueprint, render_template, request, make_response, redirect, \
    url_for, session, flash
from flask_login import current_user

from my_app.main.forms import NavigationForm
from my_app.main.functions import RenderMap

main_bp = Blueprint('main_bp', __name__)


# @main_bp.route('/', defaults={'name': 'traveler'})
# @main_bp.route('/<name>')
# def index(name):
#     if not current_user.is_anonymous:
#         name = current_user.username
#     return render_template('index.html', title="Home page",
#                            name=name)
#
#
# @main_bp.route('/navigation', methods=['GET', 'POST'])
# def navigation():
#     form = NavigationForm()
#     if request.method == 'POST':
#         map = RenderMap(form.mean.data)
#         start = form.start.data
#         end = form.end.data
#
#         flash("Well Done")
#         return redirect(url_for('main_bp.index'))
#     return render_template('navigation.html', form=form)


# @main_bp.route('/', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
# @main_bp.route('/<name>', methods=['GET', 'POST'])
# def index(name):
#     if not current_user.is_anonymous:
#         name = current_user.username
#
#     form = NavigationForm()
#     if request.method == 'POST':
#         map = RenderMap(form.mean.data)
#         start = form.start.data
#         end = form.end.data
#
#         flash("Well Done")
#         return redirect(url_for('main_bp.index'))
#
#     return render_template('navigation.html', title="Navigate",
#                            name=name, form=form)


@main_bp.route('/', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@main_bp.route('/<name>', methods=['GET', 'POST'])
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username

    form = NavigationForm()
    if request.method == 'POST':
        return redirect(url_for('main_bp.map'))

    return render_template('navigation.html', title="Navigate",
                           name=name, form=form)


@main_bp.route('/map', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@main_bp.route('/map/<name>', methods=['GET', 'POST'])
def map(name):
    if not current_user.is_anonymous:
        name = current_user.username

    mean = request.form.get('mean')
    start = request.form.get('start')
    end = request.form.get('end')
    text = "You are using {}, from {} to {}".format(mean, start, end)
    # if request.method == 'POST':
    #     return redirect(url_for('main_bp.index'))
    return render_template('navigation_map.html', title="Navigation map 1",
                           name=name, message=text)


# @main_bp.route('/nav', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
# @main_bp.route('/nav/<name>', methods=['GET', 'POST'])
# def nav(name):
#     if not current_user.is_anonymous:
#         name = current_user.username
#
#     mean = request.form.get('mean')
#     start = request.form.get('start')
#     end = request.form.get('end')
#     text = "again, You are using {}, from {} to {}".format(mean, start, end)
#     return render_template('navigation_map.html', title="Navigation map 2",
#                            name=name, message=text)
