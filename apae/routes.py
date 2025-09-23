from flask import Flask, render_template
from apae import app

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/historia')
def story():
    return render_template('story.html')

@app.route('/clinica')
def clinic():
    return render_template('clinic.html')

@app.route('/seja_voluntario')
def voluntary():
    return render_template('voluntary.html')