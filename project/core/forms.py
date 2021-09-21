from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user

class LoginForm(FlaskForm):
    user_name = StringField(label='', validators=[DataRequired(),Email()])
    password = PasswordField(label='', validators=[DataRequired()])
    submit = SubmitField('Log In')
