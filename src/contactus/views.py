from src import app
from flask import render_template, request, redirect, url_for


@app.route("/contact-us/")
def contact_us():
    return render_template('contactus.html', form=form)


