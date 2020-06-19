from flask_wtf import Form, validators
from wtforms import TextField, StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, EqualTo, Length, InputRequired, length


class register(Form):
      firstname = StringField('Firstname',validators=[DataRequired()])
      lastname= StringField('Lastname',validators=[DataRequired()])
      birthdate = DateField('Birthdate', format='%m/%d/%Y',validators=[DataRequired()])
      email =StringField('Email',validators=[DataRequired()])
      password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match'),length(min=6)])
      confirm = PasswordField('Repeat password',validators=[DataRequired()])
      submit =SubmitField('Register')
