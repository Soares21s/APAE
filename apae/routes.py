from flask import Flask, render_template
from apae import app

@app.route('/')
def homepage():
    return render_template("homepage.html")
