from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, FileField
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from wtforms.validators import DataRequired, ValidationError

from my_app import photos
# from my_app.models import Profile


class ProfileForm(FlaskForm):
    """ Class for the profile form """
    # username = StringField(label='Username', validators=[DataRequired()])
    bio = TextAreaField(label='Bio', description='Write something about yourself')
    photo = FileField('Profile picture', validators=[FileAllowed(photos, 'Images only!')])
    # tubeline = QuerySelectField(label='Your favourite tube line', query_factory=lambda: TubeLine.query.all(), \
    #                             get_label='tubeline', allow_blank=True)

    # def validate_username(self, username):
    #     profile = Profile.query.filter_by(username=username.data).first()
    #     if profile is not None:
    #         raise ValidationError('Username already exists, choose another one')

