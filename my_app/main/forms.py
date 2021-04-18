from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import data_required, DataRequired


class NavigationForm(FlaskForm):
    mean = SelectField('Select your mean:', choices=['Bus', 'Tube'], validators=[DataRequired()])
    start = SelectField('Start', choices=[None, 'Euston', "King's Cross"],
                        validators=[DataRequired()])
    end = SelectField('End', choices=[None, 'Victoria', "Angel"], validators=[DataRequired()])
    # start = QuerySelectField(label='Your favourite tube line', query_factory=lambda: TubeLine.query.all(), \
    #            get_label='tubeline', allow_blank=True)
    # end = QuerySelectField(label='Your favourite tube line', query_factory=lambda: TubeLine.query.all(), \
    #            get_label='tubeline', allow_blank=True)
