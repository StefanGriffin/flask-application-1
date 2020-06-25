from src import app
from flask import render_template 

@app.route("/about-us/")
def aboutus():
     return render_template('aboutus.html')


