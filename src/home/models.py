# from flask_sqlalchemy import SQLAlchemy
from src import db

# db = SQLAlchemy(app)


class EmailSignup(db.Model):

<<<<<<< HEAD
    # __tablename__ = "allusers"
=======
    __tablename__ = "allusers"
>>>>>>> Flask-with-PostgreSQL

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email




