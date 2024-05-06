from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
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
    team_count = team_member.objects.all().count()
    dashboard_data={"team_count":team_count}
    return render(request , 'Dashboard.html',{"data":dashboard_data})

def Signup(request):
    return render(request , 'SignUp.html')

def Calender(request):
    return render(request , 'Calender.html')

@api_view(["GET"])
def list_team(request):
    
    query_data=team_member.objects.filter()[0:10]
    serialize_data = [obj.__dict__ for obj in query_data]
    column = list(serialize_data[0].keys())
    column.pop(0)
    table_data={}
    table_data["data"] = serialize_data
    table_data["col"] = column.pop(0)
    return render(request , 'team.html',{"query_data":query_data,"cols":column})


@api_view(["get"])
def team_table_page(request):
    page_number = request.GET.get('page_number', 1)
    item_per_page = 10
    start = (int(page_number) - 1) * item_per_page
    end = int(page_number) * item_per_page
    query_data = team_member.objects.all()[start:end]

    serialize_data = [model_to_dict(obj) for obj in query_data]

    columns = list(serialize_data[0].keys())

    columns.remove('member_id')

    response_data = {
        "data": serialize_data,
        "col": columns
    }
    print("kkkkkkkkkkkk",response_data)
    return JsonResponse(response_data, status=200)



def add_case(request):
    print(json.loads(request.body))
    data = json.loads(request.body)

@api_view(["POST","GET"])
def Addmember(request):
    try:
        if request.method == "POST":
            data_list = json.loads(request.body)
            len(data_list)
            for data in data_list:
                if not team_member.objects.filter(email=data["email"]).exists():
                    flag=True
                else:
                    flag=False
                    break
            if flag:
                for data in data_list:
                    last_member=team_member.objects.last()
                    if last_member:
                        member_id = last_member.member_id+1
                    else:
                        member_id=1
                    tem_obj = team_member(member_id=member_id,first_name=data["firstName"],last_name=data["last_name"],designation=data["designation"],email=data["email"],
                                        number = data["number"]
                                        )
                    tem_obj.save()
                return JsonResponse({"message":"Team Added Successfully","status":200},status=200)
                
            else:
                return JsonResponse({"message":"Email Already Exists","status":404},status=404)
    except Exception as e:
        return JsonResponse({"message":e.__str__(),"status":500},status=500)

    return render(request , 'AddMember.html')


@api_view(["GET"])
def Teams(request):
    page_number = 1
    item_par_page =2
    team_member.objects.filter()[page_number-1*item_par_page:page_number*item_par_page]
    print("rrrrrrrrrrrrrr",team_member)
    return render(request,"team.html")

def Advocates(request):
    return render(request,"Advocate.html")

def NewAdvocate(request):
    return render(request,"NewAdvocate.html")