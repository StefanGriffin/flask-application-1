from flask import render_template
from src import app

@app.route("/")
def home():
    return render_template('base.html')
    