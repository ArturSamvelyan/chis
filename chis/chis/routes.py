from flask import render_template, request, url_for, flash, redirect, abort
from chis import app, socketio
from flask_socketio import send

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
	text = request.form['text']
	processed_text = text.upper()
	return processed_text

@app.route('/join')
def enter_token():
	#text = request.form['username']
    pass

@app.route('/room')
def room():
	return render_template('room.html') 

@app.route('/room/<name>')
def room_n(name):
	if not name:
		abort(404)
	return '<h1> Welcome to %s room!</h1>' % name

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

