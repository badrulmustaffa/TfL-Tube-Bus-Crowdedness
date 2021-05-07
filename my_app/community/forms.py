from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import TextAreaField, FileField
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from wtforms.validators import DataRequired, ValidationError

from my_app import photos



class ProfileForm(FlaskForm):
    """ Class for the profile form """
    bio = TextAreaField(label='Bio', description='Write something about yourself')
    photo = FileField('Profile picture', validators=[FileAllowed(photos, 'Images only!')])


