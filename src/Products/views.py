from src import app
from flask import render_template, request, redirect, url_for


@app.route("/products/")
def products():
    return render_template('products.html', form=form)


