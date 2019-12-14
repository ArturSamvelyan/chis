from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ktoprocheltotosel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

from chis import routes