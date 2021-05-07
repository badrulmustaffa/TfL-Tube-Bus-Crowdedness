from flask import render_template
from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from my_app.models import *
from my_app import app
from my_app.forum.comments_forms import CommentForm
import json
from datetime import datetime as dt

forum_bp = Blueprint('forum_bp', __name__, url_prefix='/forum')


@forum_bp.route('/', defaults={'name': 'traveler'})
@login_required
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username
    return render_template('index.html',
                           title='Forum page',
                           message='This page is still empty',
                           name=name)


@forum_bp.route('/post', methods=['GET', 'POST'])
def post():
    with open("my_app/static/comments.json", 'r') as file:
        comments = json.load(file)

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data.strip()
        timestamp = dt.now().strftime('%c')
        comments[timestamp] = comment
        with open('app/static/comments.json', 'w') as outfile:
            json.dump(comments, outfile)

    return render_template('comments_forum.html', form=form, comments=comments)
