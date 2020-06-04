# from django import forms
# from .models import User
#
# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','email']
#

from django import forms
from .models import User_info
from mongodbforms import DocumentForm

class NewUserForm(DocumentForm):
    class Meta():
        document=User_info
        fields= ('first_name', 'last_name','email')
