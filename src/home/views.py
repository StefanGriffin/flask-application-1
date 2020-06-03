import json
from flask import render_template, request
from src import app
from .forms import landingForm



@app.route("/", methods=['GET', 'POST'])
def home():
    form = landingForm()
    if form.validate_on_submit():
        print(form.full_name.data)
        print(form.email.data)
    return render_template('home.html', form=form)

    

