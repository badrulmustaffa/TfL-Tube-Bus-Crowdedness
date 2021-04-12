from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from my_app import db


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
    photo = db.Column(db.Text)
    bio = db.Column(db.Text)
    username = db.Column(db.Text, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# class TubeLine(db.Model):
#     __tablename__ = "tubeline"
#     index = db.Column(db.Text, nullable=False, primary_key=True)
#     tubeline = db.Column(db.Text, nullable=False)
#
#     def __repr__(self):
#         return self.tubeline
