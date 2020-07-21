
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# csrf = CSRFProtect(app)


app.debug = True

# # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:patrocle34@localhost/fweb1'

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# db = SQLAlchemy(app)

# # db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
# # db_uri = 'sqlite:///{}'.format(db_path)

# # url_for('static', filename='style.css')

# app.config.update(dict(
#     SECRET_KEY="SECRET",
#     WTF_CSRF_SECRET_KEY='05cab3d7-5f31-471f-a3b1-366ebb42440c',
# ))
