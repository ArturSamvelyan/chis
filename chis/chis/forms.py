from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UsernameForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=2, max=20)],
    render_kw={'placeholder':'Enter your name'})
    submit_join = SubmitField('Join Event')
    submit_create = SubmitField('Create Event')

class RoomNameForm(FlaskForm):
    name = StringField('Room_name', 
    validators=[DataRequired(), Length(min=3, max=20)],
    render_kw={'placeholder':'Enter room token'}) 
    submit = SubmitField('Join Event')
