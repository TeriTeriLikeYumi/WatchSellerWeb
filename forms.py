from flask_wtf import FlaskForm 
from wtforms import PasswordField,StringField
from wtforms.validators import DataRequired, EqualTo

# REGISTER FORM CREATE FROM USER_FORM
class RegisterForm(FlaskForm):
    password = PasswordField('Password',validators=[DataRequired()])
    comfirm = PasswordField('Repeat Password',validators=[EqualTo('password',message='Passwords must match')])
    
# LOGIN FORM CREATE FROM USER_FORM
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])