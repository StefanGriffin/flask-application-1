# from flask_sqlalchemy import SQLAlchemy
from src import db

# db = SQLAlchemy(app)


class EmailSignup(db.Model):

    __tablename__ = "allusers"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def save(self, commit=True):
        # works for both create and update
        if commit:
            instance = self
            if not instance.id:
                db.session.add(instance)
            try:
                db.session.commit()
            except Exception as e:
                print("Exception occured\n", e, '\n')
                db.session.rollback()
            return True
        return False
