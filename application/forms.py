from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class TodoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    completed = SelectField('Completed', choices=[('False', 'False'), ('True', 'True')])
    validators = [DataRequired()]
    submit = SubmitField('Add Todo')
    