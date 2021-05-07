from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class CommentForm(FlaskForm):
    comment = TextField('Comment', widget=TextArea(), validators=[DataRequired()])
    reason = SelectField(choices=['Question', 'Complaint'], validators=[DataRequired()])
