from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)



# don`t share these in a production environment 
# secret key
# wtf csrf secret key

app.config.update(dict(
    SECRET_KEY="c003d035-3181-4fb2-b9ea-91b09f207189",
    WTF_CSRF_SECRET_KEY='05cab3d7-5f31-471f-a3b1-366ebb42440c'

))


from .views import *
from .home.views import *
from .jobs.views import *
from .profiles.views import *










    










