from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class NewAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year_of_birth = IntegerField('Year of Birth', validators=[DataRequired()])
    submit = SubmitField('Submit')
