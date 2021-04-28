# from datetime import datetime
import flask
from flask import Blueprint, render_template, request, make_response, redirect, \
    url_for, session, flash
from flask_login import current_user

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
#     return render_template('', form=form)


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
#     return render_template('', title="Navigate",
#                            name=name, form=form)


# @main_bp.route('/', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
# @main_bp.route('/<name>', methods=['GET', 'POST'])
# def index(name):
#     if not current_user.is_anonymous:
#         name = current_user.username
#
#     return render_template('index.html', title="Navigate",
#                            name=name, message='This page is under construction')


@main_bp.route('/', defaults={'name': 'traveler'})
@main_bp.route('/<name>')
def index(name):
    return redirect('/navigation_dash/')


@main_bp.route('/navigation/<mean>/<start>/<end>', methods=['GET', 'POST'])
def navigation_process(mean, start, end):
    text = "The user is requesting for {} route, from {} to {}" .format(mean, start, end)
    return render_template('index.html', title="Navigation finder",
                           name='Bengong', message=text)
