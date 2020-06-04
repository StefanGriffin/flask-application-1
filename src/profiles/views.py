from flask import render_template
from src import app


@app.route("/users/<username>/")
def profile_detail(username):
    context = {"user": username}
    if username == 'griffins':
        context["right_user_msg"] = "Yeah, he is good"
    return render_template('profiles_detail.html', context=context)


@app.route("/users/")
def profiles_list():
    return render_template('profiles_list.html')


@app.route("/users/")
def base():
    return render_template('base.html')
