from datetime import datetime
from chis import db
import redis
import rq


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(25), unique=True, nullable=False)

	def __repr__(self):
		return f"User('{self.id}', '{self.username}')"

class Room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.Integer, unique=True)
	
	def __repr__(self):
		return f"Room('{self.id}', '{self.token}')"

