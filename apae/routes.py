from flask import Flask, render_template
from apae import app

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/projetos')
def story():
    return render_template('program.html')

@app.route('/clinica')
def clinic():
    return render_template('clinic.html')

@app.route('/seja_voluntario')
def voluntary():
    return render_template('voluntary.html')