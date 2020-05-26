from src import app

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/contact-us/")
def contact_us():
    return "<h1>Contact Us</h1>"

@app.route("/about-us/")
def about_us():
    return "<h1>about-us</h1>"




