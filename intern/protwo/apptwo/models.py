# from django.db import models
# import json
# # SuperUserInformation
# # User: harshita
# # Email: harshita44441@gmail.com
# # Password: harshita@22
#
# # Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=128)
#     last_name = models.CharField(max_length=128)
#     email = models.EmailField(max_length=254,unique=True)
from django.db import models
from mongoengine import *
from mongodbforms import DocumentForm
import os
import json
connect(
    db= "mydb",
    username= "harshita",
    password= "harshita@22",
    host="mongodb+srv://harshita:harshita%4022@harshita-4bfdh.mongodb.net/yoyo?authSource=admin&replicaSet=harshita-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
)
class User_info(Document):
    first_name=StringField(max_length=100)
    last_name=StringField(max_length=100)
    email=EmailField(max_length=100)



def json(self):
    form_dict= {
    "first_name" : self.first_name,
    "last_name" : self.last_name,
    "email" : self.email,
    }
    return json.dumps(form_dict)
