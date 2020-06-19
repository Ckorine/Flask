from mongoengine import *
from wtforms.fields.html5 import DateField


class User(Document):
    firstname= StringField(required=True, max_length=30)
    lastname = StringField(required=True, )
    birthdate= DateField(required=True,)
    email= StringField(required=True, )
    password = StringField(required=True, )
