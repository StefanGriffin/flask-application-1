import json
from flask import render_template, request, redirect, url_for
from src import app
from .forms import LandingForm, ViewItemsForm
from .models import EmailSignup


# @app.route("/", methods=['GET', 'POST'])
# def home():
#     form = LandingForm()
#     if form.validate_on_submit():
      
#         data = {
#             "full_name": form.full_name.data,
#             "email": form.email.data
#         }

#         obj = EmailSignup.query.filter_by(email=form.email.data).first()
#         if obj is None:
#             obj = EmailSignup(**data) # (full+name=, email=)
#             obj.save()
        
#         return redirect('/success')
#     return render_template('home.html', form=form)

# @app.route("/item/", methods=['GET', 'POST'])
# def item_list():
#     form = ViewItemsForm()
#     return render_template("items/list.html", form=form, object_list=[])
#     if form.validate_on_submit():
#         object_list = EmailSignup.query.all()
#         return render_template("items/list.html", form=None, object_list=object_list)
#     return render_template("items/list.html", object_list=object_list)