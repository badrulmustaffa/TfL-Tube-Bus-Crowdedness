from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired


#class QuestionComplaint(FlaskForm):

    #content = TextAreaField(validators=[DataRequired()])
    #submit = SubmitField()


class CreatePostForm(FlaskForm):
    content = TextAreaField(label='Post', description='Add content here', validators=[DataRequired()])
    reason = SelectField(choices=['Question', 'Complaint'], validators=[DataRequired()])
    #submit = SubmitField()


#class EditPostForm(CreatePostForm):
    #pass
