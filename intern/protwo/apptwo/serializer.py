# from rest_framework import serializers
# from .models import User
#
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta():
#         model=User
#         fields=["name","address","email"]


from rest_framework_mongoengine import serializers
from .models import User_info

class User_infoSerializer(serializers.DocumentSerializer):

    class Meta():
        model=User_info
        fields=("first_name","last_name","email")
