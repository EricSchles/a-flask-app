#!/usr/bin/python

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Guess The Language!</h1>'

@app.route('/guess/<init:id>')
def guess(id):
	return('<h1>Guess The Language!</h1>'
			'<p>My guess: {0}</p>').format(guesses[id])

if __name__ == '__main__':
	app.run(debug=True)