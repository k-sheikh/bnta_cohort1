from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired


class NewAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year_of_birth = IntegerField('Year of Birth', validators=[DataRequired()])
    submit = SubmitField('Submit')


class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
