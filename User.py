from mongoengine import *
class User(Document):
    firstname= StringField(required=True, max_length=30)
    lastname = StringField(required=True, )
    birthdate= DateField(required=True,)
    email= StringField(required=True, )
    password = StringField(required=True, )
