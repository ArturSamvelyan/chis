from flask import render_template, request, url_for, flash, redirect, abort
from chis import app, socketio
from chis.forms import UsernameForm, RoomNameForm
from flask_socketio import send
from random import random

@app.route('/', methods=['GET', 'POST'])
def index():
	form = UsernameForm()
	if form.validate_on_submit():
		print('validate')
		#user = User(username=form.username.data)
		#db.session.add(user)
		#db.session.commit()
		if form.submit_join.data:
			return redirect('join')
		if form.submit_create.data:
			print('blyat')
			return redirect('room/suka')
	return render_template('index.html', form=form)

@app.route('/join', methods=['GET', 'POST'])
def join():
	form = RoomNameForm()
	if form.validate_on_submit():
		return redirect('room/%s'%form.name.data)
	return render_template('join.html', form=form)


@app.route('/room/<name>')
def room(name):
	return render_template('room.html') 
'''
@app.route('/room/<name>')
def room_n(name):
	if not name:
		abort(404)
	return '<h1> Welcome to %s room!</h1>' % name
'''

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

