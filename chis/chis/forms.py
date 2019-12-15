from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UsernameForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)])
    submit_join = SubmitField('Join Event')
    submit_create = SubmitField('Create Event')

class RoomNameForm(FlaskForm):
    username = StringField('Room_name', 
    validators=[DataRequired(), Length(min=3, max=20)]) 
