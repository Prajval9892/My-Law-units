from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from datetime import datetime
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

def bills(request):
    return render(request,'Bills.html')

def newbill(request):
    return render(request,'NewBill.html')

def alltodo(request):
    case_obj = case.objects.all()
    all_to_do = ToDO.objects.all()
    adv_obj = Advocate.objects.all()
    data_to_send_list=[]
    pending_count = ToDO.objects.filter(status="pending",end_date__gt=datetime.now().date()).count()
    upcoming_count = ToDO.objects.filter(status="pending",end_date__lt=datetime.now().date()).count()
    comp_count = ToDO.objects.filter(status="comp").count()
    all_count = ToDO.objects.all().count()

    count = {"pending_count":pending_count,"upcoming_count":upcoming_count,"comp_count":comp_count,"all_count":all_count}

    for to_do in all_to_do:
        data_to_send={}
        data_to_send["tital"] = to_do.case_id.tital
        data_to_send["advocate_name"] = to_do.advocate_name
        data_to_send["assign_by"] = to_do.assign_by
        data_to_send["end_date"] = to_do.end_date
        data_to_send["id"] = to_do.to_do_id
        if to_do.status=="comp":
            data_to_send["status"] = "comp"
        elif to_do.end_date>datetime.now().date():
            data_to_send["status"] = "expired"
        elif to_do.status=="pending":
            data_to_send["status"] = "pending"
        
        data_to_send_list.append(data_to_send)
    return render(request,"AllToDo.html",{"case_obj":case_obj,"to_do_list":data_to_send_list,"count":count,"adv_obj":adv_obj})

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
    data_base = request.GET.get('database', None)
    item_per_page = 1
    start = (int(page_number) - 1) * item_per_page
    end = int(page_number) * item_per_page
    if data_base:
        if data_base=="Team":
            query_data = team_member.objects.all()[start:end]
        elif data_base == "Advocate":
            query_data = Advocate.objects.all()[start:end]

    serialize_data = [model_to_dict(obj) for obj in query_data]

    columns = list(serialize_data[0].keys())

    columns=["No","Full Name","Email","Number","Company Name"]

    response_data = {
        "data": serialize_data,
        "col": columns
    }
    return JsonResponse(response_data, status=200)


@api_view(["POST","GET"])
def add_case(request):
    # try:
    if request.method == "POST":
        n_data = json.loads(request.body)
        ndata=n_data
        new_case=case(court=ndata["court"],case_type=ndata["case-type"],case_number=ndata["case_number"],cnr=ndata["crn_no"],respondent=ndata["Respondent-1"],
                        high_court=ndata["high_court"],state=ndata["stateDropdown"],district=ndata["districtDropdown"],court_establishment=ndata["Court-Establishment"],year=ndata["year"],Petitioner=ndata["petitioner-1"],date_of_filling=ndata["date-filling-1"],court_hall=ndata["case-hall"],floor=ndata["case-floor"],
                        classification=ndata["classification"],tital=ndata["Title"],disc=ndata["description"],Before_Honble_Judg=ndata["Honble_Judge"],
                        ref_by=ndata["ref_by"],section=ndata["Section"],Priority=ndata["Priority"],under_act=ndata["Act"],under_section=ndata["under-section"],fir_police_station=ndata["FIR_Police_station"],
                        fir_number=ndata["FIR_no"],fir_year=ndata["FIR_year"],affidavit_vakalat_date=ndata["affidavit-vakalath-date"])
        new_case.save()
        newcases2=case.objects.get(case_number=ndata["case_number"])
        for ndata in n_data ["opponent_list"]:
            newcase1=opponent(full_name=ndata["full_name"],email=ndata["email"],phone_number=ndata["phone"],case=newcases2)
            newcase1.save()
        
        
        for ndata in n_data["advocate_detail"]:
            advt_detail=opponent_advocate(full_name=ndata["full_name"],email=ndata["email"],phone_number=ndata["phone"],case=newcases2)
            advt_detail.save()
            
    # except Exception as e:
    #     return JsonResponse({"message":e.__str__(),"status":500},status=500)
    return render(request,"Newcase.html")

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
    return render(request,"team.html")

def Advocates(request):
    query_data=Advocate.objects.filter()
    column=[]
    serialize_data=[]
    if query_data:
        query_data = query_data[0:10]
        serialize_data = [obj.__dict__ for obj in query_data]
        column = list(serialize_data[0].keys())
        column.pop(0)
    table_data={}
    table_data["data"] = serialize_data
    table_data["col"] = column
    col = ["No","Full Name","Email","Number","Company Name"]
    return render(request , 'Advocate.html',{"query_data":query_data,"cols":col})

@api_view(["POST","GET"])
def NewAdvocate(request):
    # try:
    if request.method == "POST":
        new_advt = json.loads(request.body)
        data=new_advt
        advt_obj = Advocate(fullname=data["full_name"],email=data["email"],number=data["phone_no"],age=data["adv_age"],
                                father_name = data["father_name"],company_name=data["company_name"],website=data["website_1"],
                                tin=data["tin_1"],gst=data["gst_id_no"],pan=data["permanent-acc-no"],hourly_rate=data["hourly_rate"],
                                )
        advt_obj.save()
        new_advocate1=Advocate.objects.get(email=data["email"])
        
        advt_obj1=home_address(address_line1=data["home_address_1"],address_line2=data["home-address-2"],country=data["country-2"],state=data["state-2"],city=data["city2"],
                            zip_postal_code=data["home_zip_postal_code"],advocate=new_advocate1)
        
        advt_obj1.save()
        
        advt_obj2=office_address(address_line1=data["address_line_1"],address_line2=data["address_line_2"],country=data["country-1"],state=data["state1"],
                            city=data["city1"],zip_postal_code=data["zip_postal_code"],advocate=new_advocate1)
        advt_obj2.save()
        
        
        for data in new_advt ["point_of_con"]:
            advobj=contact_point(full_name=data["fullName"],contact_email=data["email"],phone_number=data["phoneNo"],designation=data["designation"],advocate=new_advocate1)
            advobj.save()
        
        return JsonResponse({"message":"Team Added Successfully","status":200},status=200)
    # except Exception as e:
    #     return JsonResponse({"message":e.__str__(),"status":500},status=500)
    return render(request,"NewAdvocate.html")


@api_view(["GET"])
def delete_record(request):
    id = request.GET.get("id")
    database = request.GET.get("database")
    if team_member.objects.filter(member_id=id).exists():
        if database == "team_member":
            obj=team_member.objects.get(member_id=id)
        elif database == "Advocate":
            obj=Advocate.objects.get(advocate_id=id)
        obj.delete()
        return JsonResponse({"message":"Team Member deleted successfully","status":200},status=200)
    else:
        return JsonResponse({"message":"Team Member Not Found","status":404},status=404)
    


@api_view(["POST"])
def add_todo(request):
    data = json.loads(request.body)
    case_obj=case.objects.get(case_number=data["case_name"])
    to_do_obj = ToDO(case_id=case_obj,advocate_name=data["advocate"],description=data["description"],start_date=data["start_date"],end_date=data["end_date"],assign_by=request.user)
    to_do_obj.save()
    return JsonResponse({"message":"TODO Added successfully","status":200},status=200)

@api_view(["POST"])
def change_to_status(request):
    data = json.loads(request.body)
    to_obj = ToDO.objects.get(to_do_id=data["id"])
    to_obj.status = data["status"]
    to_obj.save()
    return JsonResponse({"message":"TO DO Updated Successfully","status":200},status=200)