from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import data_required


class NavigationForm(FlaskForm):
    mean = SelectField(label='Select your mean:', validators=[data_required()])
    # start = QuerySelectField(label='Your favourite tube line', query_factory=lambda: TubeLine.query.all(), \
    #            get_label='tubeline', allow_blank=True)
    # end = QuerySelectField(label='Your favourite tube line', query_factory=lambda: TubeLine.query.all(), \
    #            get_label='tubeline', allow_blank=True)
