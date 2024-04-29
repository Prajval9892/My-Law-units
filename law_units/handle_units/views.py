from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def user_login(request):
    return render(request,"Login.html")
