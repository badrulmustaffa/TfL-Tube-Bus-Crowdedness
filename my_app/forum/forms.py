from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField, validators
from wtforms.validators import DataRequired


'''
class CreatePostForm(FlaskForm):
    content = TextAreaField(label='Post', description='Add content here', validators=[DataRequired()])
    reason = SelectField(choices=['Question', 'Complaint'], validators=[DataRequired()])
    submit = SubmitField()
'''


class ThreadForm(FlaskForm):
    title = StringField("Title", [validators.required(), validators.length(max=150)])
    description = TextAreaField("description", [validators.required()])


class PostForm(FlaskForm):
    content = StringField("content", [validators.required()])


class ForumForm(FlaskForm):
    name = StringField("Forum name:", [validators.DataRequired(message="Category name field is required!")])
    description = StringField("Forum description:", [validators.DataRequired(message="Forum description field is required!")])


class CategoryForm(FlaskForm):
    name = StringField("Category name:", [validators.DataRequired(message="Category name field is required!")])
