#!/usr/bin/python

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import form
from wtforms.fields import RadioField, SubmitField

app = Flask(__name__)
questions = ['Is it compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']

@app.route('/')
def index():
	return render_template('index.html')
 
@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
	if request.method=='POST':
		if request.form['answer'] == 'yes':
			return redirect(url_for('question', id=id+1))
	return render_template('question.html', question=questions[id])

@app.route('/guess/<int:id>')
def guess(id):
	return render_template('guess.html', guess=guesses[id])
if __name__ == '__main__':
	app.run(debug=True)
	#run on development web server, use this
	#app.run(host='0.0.0.0', port=5000, debug=True)