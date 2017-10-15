from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django .template import loader
from .models import StudentComplain , s_user_name, c_user_name,supvisor_user_name,w_user_name,feedback
from django .shortcuts import render,get_object_or_404
from .forms import complain_form,login_form
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

#username_global="invaild"

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_type = request.POST.get('user_type', '')
        if user_type=='1':
            try:
                stud=s_user_name.objects.get(s_userid=username)
                print("found student")
                #user = authenticate(username = username, password = username)
                 #if stud is not None:
                  #    if stud.is_active:
                   #        login(request, stud)
                    #       return HttpResponseRedirect('/')
                     #  else:
                      #     print("The account has been disabled!")
                #else:
                    #print("The username and password were incorrect.")
                return render(request,'home/index.html')
            except s_user_name.DoesNotExist:
                stud = None
                print("not found student")
                return HttpResponse("<h5>wrong user credentials")

        elif user_type=='2':
            try:
                care=c_user_name.objects.get(c_user_id=username)
                print("found in caretaker")
                x=StudentComplain.objects.all()
                return render(request,'home/index1.html',{'x':x})
            except c_user_name.DoesNotExist:
                care = None
                print("not found in caretaker")
                return HttpResponse("<h5>wrong caretaker credentials")
        else:
            try:
                sup=supvisor_user_name.objects.get(sup_user_id=username)
                print("found in supervisor")
            except supvisor_user_name.DoesNotExist:
                sup = None
                print("not found in supervisor")
                return HttpResponse("<h5>wrong supervisor credentials")


        if user_type =='1':
            user="student"
        elif user_type=='2':
            user="caretaker"
        else:
            user="supervisor"
        return HttpResponse("<H1> username : "+ username + "</h1><H1> password : "+ password + "</h1><H1> USER type : "+ user + "</h1>")

    else:
        return render(request,'home/login.html')

def index1(request):
    return render(request,'home/home.html',{})

def index(request):
    form=complain_form()
    return render(request,'home/index.html')


def compl_form(request):
    print("inside complain_form")
    location = request.POST.get('location', '')
    specific_location = request.POST.get('specific_location', '')
    details = request.POST.get('details', '')
    x=StudentComplain(location=location,specific_location=specific_location,details=details,user_id="")

    form = complain_form(request.POST)
    if form.is_valid():
        #x=StudentComplain(com_id=form.cleaned_data['com_id'],
        #                 location=form.cleaned_data['location'],
        #                  details=form.cleaned_data['details'])
        #x.save()
        form.save(commit=True)

    return HttpResponseRedirect('/home/')

def show_data(request,comp_id):
    x=StudentComplain.objects.all()
    res=StudentComplain
    for i in x:
        if comp_id =='1':
            res=StudentComplain.objects.filter(location="HALL 1")
        elif comp_id == '2':
            res=StudentComplain.objects.filter(location="HALL 3")
        elif comp_id == '3':
           res=StudentComplain.objects.filter(location="HALL 4")
        elif comp_id == '4':
           res=StudentComplain.objects.filter(location="CC")
        elif comp_id == '5':
            res=StudentComplain.objects.filter(location="GARBAGE")
        elif comp_id == '0':
            res=StudentComplain.objects.all()
        else:
            return HttpResponse("<H5>WRONG CHOICE")

    return render(request,'home/index1.html',{'x':res})

def complaint_details(request,comp_id):
    #m1=get_object_or_404(StudentComplain,pk=comp_id)
    try:
        m1=StudentComplain.objects.get(pk=comp_id)
    except StudentComplain.DoesNotExist:
        return HttpResponse("<H1>Not a valid complaint </H1>")
    return render(request,'home/complaint_det.html',{'m1':m1})


#def show_login(request):
    #return render(request,'home/login.html')
