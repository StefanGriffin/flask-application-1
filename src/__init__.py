
import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# from .home.models import *


app = Flask(__name__)
csrf = CSRFProtect(app)


# don`t share these in a production environment
# secret key
# wtf csrf secret key

# Configure the database

app.debug = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:patrocle34@localhost/fweb1'


# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
# db_uri = 'sqlite:///{}'.format(db_path)


app.config.update(dict(
    SECRET_KEY="c003d035-3181-4fb2-b9ea-91b09f207189",
    WTF_CSRF_SECRET_KEY='05cab3d7-5f31-471f-a3b1-366ebb42440c',
))


from .profiles.views import *
from .jobs.views import *
from .home.views import *
from .views import *

