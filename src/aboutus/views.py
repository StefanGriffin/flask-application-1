from src import app
from flask import render_template, request, redirect, url_for

@app.route("/about-us/")
def about_us():
     return render_template('aboutus.html', form=form)


