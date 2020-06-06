import json
from flask import render_template, request, redirect
from src import app
from .forms import LandingForm
from .models import EmailSignup


@app.route("/", methods=['GET', 'POST'])
def home():
    form = LandingForm()
    if form.validate_on_submit():
        # print(form.full_name.data)
        # print(form.email.data)
        # data = form.data
        data = {
            "full_name": form.full_name.data,
            "email": form.email.data
        }
        # if 'csrf_token' in data:
            # del data['csrf_token']
        # if 'id' in data:
            # del data['id']
        obj = EmailSignup.query.filter_by(email=form.email.data).first()
        if obj is None:
            obj = EmailSignup(**data) # (full+name=, email=)
            obj.save()
        # form = LandingForm()
        # return render_template('home.html', form=form)
        return redirect("/item/{}".format(obj.id))
    return render_template('home.html', form=form)

'''
create email obj instance via form
saved in database
in databases, we have objects with ids in models.py
ids == primary keys
primary keys to lookup in database
use dynamic url routing to lookup object in databses

'''
@app.route("/items/", methods=['GET'])
def item_list():
    object_list = EmailSignup.query.all()
    return render_template("items/list.html", object_list=object_list)

@app.route("/item/", methods=['GET'])
def item_list_redirect():
    return redirect("/items/")


@app.route("/items/<int:id>/", methods=['GET'])
def item_detail_redirect(id):
    return redirect("/item/{}/".format(id))


@app.route('/item/<int:id>/', methods=['GET'])
def item_detail(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    return render_template('items/detail.html', instance=instance)

@app.route('/item/<int:id>/update/', methods=['GET', 'POST'])
def item_update(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    # instance.full_name -> form.full_name
    # instance.email -> form.email
    form = LandingForm(obj=instance)
    if form.validate_on_submit():
        full_name = form.full_name.data
        email = form.email.data
        instance.full_name = full_name
        instance.email = email
        instance.save()
        return redirect("/item/{}/".format(instance.id))
        # data = form.data
        # print(data)  
    return render_template('items/form.html', instance=instance, form=form)
 

@app.route('/item/<int:id>/delete/', methods=['GET', 'POST'])
def item_delete(id):
    # instance = EmailSignup.query.get(id)
    instance = EmailSignup.query.filter_by(id=id).first_or_404()
    # form
    if request.method == "POST":
        instance.delete()
        return redirect("/")
    return render_template('items/delete.html', instance=instance)
