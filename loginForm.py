from flask_wtf import Form
from wtforms import TextField, StringField, PasswordField, SubmitField

#

class loginForm(Form):
    
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Log In')