import json
from flask import render_template, request
from src import app
from .forms import landingForm
from .models import EmailSignup


@app.route("/", methods=['GET', 'POST'])
def home():
    form = landingForm()
    if form.validate_on_submit():
        # print(form.full_name.data)
        # print(form.email.data)
        data = form.data
        print(data)
        if 'csrf_token' in data:
            del data['csrf_token']
        obj = EmailSignup(**data)
        obj.save()
    return render_template('home.html', form=form)
