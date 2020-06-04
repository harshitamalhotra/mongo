# from django.shortcuts import render
# from .forms import NewUserForm
#
# def index(request):
#     return render(request,'apptwo/index.html')
#
# def help(request):
#     helpdict = {'help_insert':'HELP PAGE'}
#     return render(request,'apptwo/help.html',context=helpdict)
#
# def users(request):
#     form = NewUserForm()
#
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('ERROR FORM INVALID')
#
#     return render(request,'apptwo/users.html',{'form':form})

from django.shortcuts import render
from rest_framework.views import APIView
from .models import User_info
from .serializer import User_infoSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
from .forms import NewUserForm

def index(request):
    form=NewUserForm()


    if request.method=="POST":
        form=NewUserForm(request.POST)



        if form.is_valid():
            form.save(commit=True)



        else:
            print("ERROR")

    return render(request,'apptwo/users.html',{"form":form})


class Userlist(APIView):
    def get(self,request):
        if request.method=="GET":
            users1=User_info.objects.all()
            serial=User_infoSerializer(users1,many=True)
            return Response(serial.data)
    def post(self,request):
          if request.method=="POST":
             serializer=User_infoSerializer(data=request.data)
             if (serializer.is_valid()):
                 serializer.save()
                 return Response(serializer.data)
