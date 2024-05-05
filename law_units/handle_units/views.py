from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse
# Create your views here.

@api_view(["GET"])
def user_login(request):
    return render(request,"Login.html")

def index(request):
    return render(request,'index.html')

def cases(request):
    return render(request,'Cases.html')

def newcases(request):
    return render(request,'NewCase.html')

def home(request):
    return render(request,'Home.html')

def forgotpassword(request):
    return render(request,"ForgotPassword.html")

def completedtodo(request):
    return render(request,"{% url 'alltodo' %}")

def upcomingtodo(request):
    return render(request,"{% url 'alltodo' %}")

def alltodo(request):
    return render(request,"AllToDo.html")

def pendingtodo(request):
    return render(request,"{% url 'alltodo' %}")

def document(request):
    return render(request,"Document.html")

def newdocument(request):
    return render(request,"NewDocument.html")

def Dashboard(request):
    return render(request , 'Dashboard.html')

def Signup(request):
    return render(request , 'SignUp.html')

def Calender(request):
    return render(request , 'Calender.html')

def list_team(request):
    return render(request , 'team.html')

def add_case(request):
    print(json.loads(request.body))
    data = json.loads(request.body)

@api_view(["POST","GET"])
def Addmember(request):
    try:
        if request.method == "POST":
            data_list = json.loads(request.body)
            for data in data_list:
                tem_obj = team_member(first_name=data["firstName"],last_name=data["last_name"],designation=data["designation"],email=data["email"],
                                    number = data["number"]
                                    )
                tem_obj.save()
            return JsonResponse({"message":"Team Added Successfully","status":200},status=200)
    except Exception as e:
        return JsonResponse({"message":e.__str__(),"status":500},status=500)

    return render(request , 'AddMember.html')

def Teams(request):
    return render(request,"team.html")

def Advocates(request):
    return render(request,"Advocate.html")

def NewAdvocate(request):
    return render(request,"NewAdvocate.html")