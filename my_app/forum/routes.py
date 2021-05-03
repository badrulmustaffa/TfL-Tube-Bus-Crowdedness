from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from my_app.models import Category, Forum, Thread, db, Post, User
from collections import OrderedDict
from my_app.forum.forms import ThreadForm, PostForm, ForumForm, CategoryForm
from slugify import slugify

forum_bp = Blueprint('forum_bp', __name__, url_prefix='/forum')


@forum_bp.route('/index', defaults={'name': 'traveler'})
@login_required
def index():
    categories = Category.query.all()
    category_forums_threads = OrderedDict()
    for category in categories:
        forum_threads = OrderedDict()
        category_forums = Forum.query.filter_by(category_id=category.id).all()
        for forum in category_forums:
            threads = Thread.query.filter_by(forum_id=forum.id).all()
            forum_threads[forum] = threads
        category_forums_threads[category] = forum_threads
    return render_template("forum.html", category_forums_threads=category_forums_threads)


"""def index(name):
    if not current_user.is_anonymous:
        name = current_user.username

    form = CreatePostForm()
    if request.method == 'POST':
        return redirect(url_for('forum_bp.posts'))

    return render_template('post_forum.html', title="Forum",
                           name=name, form=form)
"""


@forum_bp.route('/posts', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def posts(name):
    if not current_user.is_anonymous:
        name = current_user.username
    form = PostForm
    return render_template('post_forum.html', title='Forum', name=name, form=form)


@forum_bp.route('/show_category', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def show_category(slug):
    category = Category.query.filter_by(slug=slug).first()
    if not category:
        abort(404)
    return render_template("showCategory.html", category=category)


@forum_bp.route('/edit_category', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def edit_category(slug):
    category = Category.query.filter_by(slug=slug).first()
    if not category:
        abort(404)
    if current_user.account_type != "administrator":
        abort(401)
    form = CategoryForm(request.form, category)
    if request.method == "GET":
        return render_template("editCategory.html", form=form)
    else:
        if request.method == "POST":
            if not form.validate():
                return render_template("createCategory.html", form=form)
            category.name = form.name.data
            category.slug = slugify(form.name.data)
            db.session.commit()
            return redirect(url_for("category.showCategory", slug=category.slug))


@forum_bp.route('/delete_category', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def delete_category(slug):
    category = Category.query.filter_by(slug=slug).first()
    if not category:
        abort(404)
    if current_user.account_type != "administrator":
        abort(401)
    if request.method == "GET":
        return render_template("delete_category_confirmation.html", category=category)
    elif request.method == "POST":
        db.session.delete(category)
        db.session.commit()
        return redirect("/index")


@forum_bp.route("/show_forum", defaults={'name': 'traveler'})
def show_forum(forum_slug):
    forum = Forum.query.filter_by(slug=forum_slug).first()
    if not forum:
        abort(404)
    forum_threads = Thread.query.filter_by(forum_id=forum.id).all()
    return render_template("showForum.html", forum=forum, forum_threads=forum_threads)


@forum_bp.route('/edit_forum', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def edit_forum(forum_slug):
    forum = Forum.query.filter_by(slug=forum_slug).first()
    if not forum:
        abort(404)
    elif not current_user.account_type == "administrator":
        abort(401)
    form = ForumForm(request.form)
    if request.method == "GET":
        return render_template("editForum.html",form=form,forum=forum)
    elif request.method == "POST":
        if not form.validate():
            return render_template("editForum.html",form=form,forum=forum)
        elif form.name.data != forum.name:
            if Forum.query.filter_by(name=form.name.data).all():
                return render_template("editForum.html",form=form,forum=forum,name_taken=True)
        forum.name = form.name.data
        forum.slug = slugify(form.name.data)
        forum.description = form.description.data
        db.session.commit()
        return redirect("/")


@forum_bp.route('/delete_forum', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def delete_forum(forum_slug):
    forum = Forum.query.filter_by(slug=forum_slug).first()
    if not current_user.account_type == "administrator":
        abort(401)
    elif not forum:
        abort(404)
    if request.method == "GET":
        return render_template("delete_forum_confirmation.html", forum=forum)
    elif request.method == "POST":
        db.session.delete(forum)
        db.session.commit()
        return redirect(url_for("index"))


@forum_bp.route('/create_post', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def create_post(thread_slug):
    thread = Thread.query.filter_by(slug=thread_slug).first()
    if not thread:
        abort(404)
    post_form = PostForm(request.form)
    if request.method == "GET":
        return render_template("createPost.html", post_form=post_form, thread=thread)
    elif request.method == "POST":
        if not post_form.validate():
            return render_template("createPost.html", post_form=post_form, thread=thread)
        post = Post(thread_id=thread.id, user_id=current_user.id, content=post_form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("thread.showThread", thread_slug=thread_slug))


@forum_bp.route('/edit_post', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    thread_slug = Thread.query.get_or_404(post.thread_id).slug
    if not post.user_id == current_user.id:
        abort(401)
    post_form = PostForm(request.form)
    if request.method == "GET":
        return render_template("editPost.html", post_form=post_form, post=post)
    elif request.method == "POST":
        if not post_form.validate():
            return render_template("editPost.html", post_form=post_form, post=post)
        post.content = post_form.content.data
        db.session.commit()
        return redirect(url_for("thread.showThread", thread_slug=thread_slug))


@forum_bp.route('/show_thread', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
def show_thread(thread_slug):
    thread = Thread.query.filter_by(slug=thread_slug).first()
    if not thread:
        abort(404)
    post_form = PostForm(request.form)
    posts_thread = Post.query.filter_by(thread_id=thread.id).all()
    post_user = OrderedDict()
    for post in posts_thread:
        post_user[post] = User.query.get_or_404(post.user_id)
    return render_template("showThread.html", thread=thread, post_user=post_user, post_form=post_form)


@forum_bp.route('/create_thread', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def create_thread(forum_slug):
    forum = Forum.query.filter_by(slug=forum_slug).first()
    if not forum:
        abort(404)
    form = ThreadForm(request.form)
    if request.method == "GET":
        return render_template("createThread.html",form=form,forum=forum)
    elif request.method == "POST":
        if not form.validate():
            return render_template("createThread.html",form=form,forum=forum)
        thread = Thread(forum_id=forum.id, user_id=current_user.id, title=form.title.data, slug=slugify(form.title.data), description=form.description.data)
        db.session.add(thread)
        db.session.commit()
        return redirect(url_for("thread.showThread",thread_slug=thread.slug))


@forum_bp.route('/edit_thread', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def edit_thread(thread_slug):
    thread = Thread.query.filter_by(slug=thread_slug).first()
    if not thread:
        abort(404)
    elif not thread.user_id == current_user.id:
        abort(401)
    form = ThreadForm(request.form)
    if request.method == "GET":
        return render_template("editThread.html", form=form, thread=thread)
    elif request.method == "POST":
        if not form.validate():
            return render_template("editThread.html", form=form, thread=thread)
        thread.title = form.title.data
        thread.slug = slugify(form.title.data)
        thread.description = form.description.data
        db.session.commit()
        return redirect(url_for("thread.showThread", thread_slug=thread.slug))


@forum_bp.route('/delete_thread', defaults={'name': 'traveler'}, methods=['GET', 'POST'])
@login_required
def delete_thread(thread_slug):
    thread = Thread.query.filter_by(slug=thread_slug).first()
    if not thread:
        abort(404)
    elif not thread.user_id == current_user.id:
        abort(401)
    forum = Forum.query.get_or_404(thread.forum_id)
    if request.method == "GET":
        return render_template("delete_thread_confirmation.html", thread=thread)
    elif request.method == "POST":
        db.session.delete(thread)
        db.session.commit()
        return redirect(url_for("forum.showForum", forum_slug=forum.slug))
