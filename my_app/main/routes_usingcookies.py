# from datetime import datetime
#
# from flask import Blueprint, render_template, request, make_response, redirect, url_for
#
# main_bp_cookies = Blueprint('main_bp', __name__)
#
#
# @main_bp_cookies.route('/', defaults={'name': 'traveler'})
# @main_bp_cookies.route('/user/<name>')
# def index_withcookies(name):
#     if 'name' in request.cookies:
#         name = request.cookies.get('name')
#
#     return render_template('index.html', title="Home page",
#                            name=name)
#
#
# @main_bp_cookies.route('/delete_cookie')
# def delete_cookie():
#     response = make_response(redirect(url_for('main_bp.index')))
#     response.set_cookie('name', 'traveler', expires=datetime.now())
#     return response

