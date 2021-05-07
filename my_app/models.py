from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from slugify import slugify
from my_app import db
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.id} {self.username} {self.email} {self.password}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    bio = db.Column(db.Text)
    photo = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class History(db.Model):
    __tablename__ = "history"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column('created_on', db.DateTime, default=datetime.utcnow())
    mean = db.Column(db.Text)
    start = db.Column(db.Text)
    end = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Blogpost(db.Model):
    __tablename__ = "blogpost"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    slug = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name
        self.slug = slugify(name)

    def __repr__(self):
        return f"<Category {self.id}>"


class Forum(db.Model):
    __tablename__ = "forum"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    name = db.Column(db.String, unique=True)
    slug = db.Column(db.String, unique=True)
    description = db.Column(db.String)

    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.slug = slugify(name)
        self.description = description


class Thread(db.Model):
    __tablename__ = "thread"
    id = db.Column(db.Integer, primary_key=True)
    forum_id = db.Column(db.Integer, db.ForeignKey(Forum.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    title = db.Column(db.String(150))
    slug = db.Column(db.String)
    description = db.Column(db.String)
    created_on = db.Column('created_on', db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Thread {self.id}>"


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    thread_id = db.Column(db.Integer, db.ForeignKey(Thread.id))
    content = db.Column(db.String)
    created_on = db.Column('created_on', db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"<Post {self.id}"
