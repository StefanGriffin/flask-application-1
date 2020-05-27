from flask_wtf import FlaskForm
from wtforms import StringField, validators


class landingForm(FlaskForm):
    full_name = StringField('Full name', validators=[
        validators.DataRequired(
            message='Your full name is required'
        )
    ])
    email = StringField('Email', validators=[
        validators.DataRequired(
            message='Your email is required'
        )
    ])

