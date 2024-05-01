from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def user_login(request):
    return render(request,"Login.html")

def index(request):
    return render(request,'index.html')

def cases(request):
    return render(request,'Cases.html')

def home(request):
    return render(request,'Home.html')

def forgotpassword(request):
    return render(request,"ForgotPassword.html")

