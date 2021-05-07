from flask import render_template, request, redirect, url_for, Blueprint
from datetime import datetime

from my_app import db
from my_app.models import Blogpost

blog_bp = Blueprint('blog_bp', __name__, url_prefix='/community')

@blog_bp.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('blog_index.html', posts=posts)


@blog_bp.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('blog_post.html', post=post)


@blog_bp.route('/about')
def about():
    return render_template('blog_about.html')


@blog_bp.route('/add')
def add():
    return render_template('blog_add.html')


@blog_bp.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))
