from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from my_app.forum.forms import CreatePostForm


forum_bp = Blueprint('forum_bp', __name__, url_prefix='/forum')


@forum_bp.route('/', defaults={'name': 'traveler'})
@login_required
def index(name):
    if not current_user.is_anonymous:
        name = current_user.username

    form = CreatePostForm()
    if request.method == 'POST':
        return redirect(url_for('forum_bp.posts'))

    return render_template('post_forum.html', title="Forum",
                           name=name, form=form)


@forum_bp.route('/posts', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def posts(name):
    if not current_user.is_anonymous:
        name = current_user.username
    form = CreatePostForm
    return render_template('post_forum.html', title='Forum', name=name, form=form)
