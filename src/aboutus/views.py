from src import app
from flask import render_template, request, redirect, url_for

@app.route("/about-us/")
def aboutus():
     return render_template('aboutus.html', form=form)


