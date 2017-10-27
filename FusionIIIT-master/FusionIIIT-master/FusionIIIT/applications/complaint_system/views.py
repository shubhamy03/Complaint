from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import StudentComplain, Workers, Caretaker
from applications.globals.models import ExtraInfo, User
from django.contrib.auth import authenticate, login, logout


def complaint(request):

    if request.method == 'POST':
        comp_type = request.POST.get('complaint_type', '')
        location = request.POST.get('Location', '')
        specific_location = request.POST.get('specific_location', '')
        details = request.POST.get('details', '')

        y=ExtraInfo.objects.get(id="2015001")
        x=StudentComplain(complainer=y,
                          complaint_type=comp_type,
                          location=location,
                          specific_location=specific_location,
                          details=details)

        x.save()

        history = StudentComplain.objects.all()
        return render(request, "complaintModule/complaint.html", {'history': history})

    else:
        history = StudentComplain.objects.order_by('-id')
        return render(request, "complaintModule/complaint.html", {'history': history})


def assign_worker(request, comp_id):

    if request.method == 'POST':
        complaint_finish = request.POST.get('complaint_finish', '')
        worker_id = request.POST.get('assign_worker', '')
        w = Workers.objects.get(id=worker_id)
        # StudentComplain.objects.get(id=comp_id).update(complaint_finish='complaint_finish', worker_id='worker_id')
        StudentComplain.objects.select_for_update().filter(id=comp_id).\
            update(complaint_finish='complaint_finish', worker_id='worker_id')
        return HttpResponseRedirect('./')
    else:
        try:
            detail = StudentComplain.objects.get(id=comp_id)
            worker = ''
            flag = ''
            temp = detail.location
            try:
                care = Caretaker.objects.get(area = temp)
                if Workers.objects.filter(caretaker_id=care).count() == 0:
                    flag = 'no_worker'
                else:
                    worker = Workers.objects.filter(caretaker_id=care)

            except Caretaker.DoesNotExist:
                flag = 'no_worker'

        except StudentComplain.DoesNotExist:
            return HttpResponse("<H1>Not a valid complaint </H1>")
        return render(request, "complaintModule/assignworker.html", {'detail': detail, 'worker': worker, 'flag': flag})


def check(request):
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        user = authenticate(username=u, password=p)
        if user is not None:
            if user.is_active:
                login(request, user)
                a = User.objects.get(username=u)
                b = ExtraInfo.objects.get(user=a)
                if b.user_type == 'student':
                    return HttpResponseRedirect('/complaint/user/'+b.id)
                else:
                    return HttpResponseRedirect('/complaint/caretaker/'+b.id)
        else:
            return HttpResponse("<h1>wrong user credentials</h1>")
    else:
        return HttpResponseRedirect('/login/')


def user(request, comp_id):
    if request.method == 'POST':
        comp_type = request.POST.get('complaint_type', '')
        location = request.POST.get('Location', '')
        specific_location = request.POST.get('specific_location', '')
        details = request.POST.get('details', '')

        y = ExtraInfo.objects.get(id=comp_id)
        x=StudentComplain(complainer=y,
                          complaint_type=comp_type,
                          location=location,
                          specific_location=specific_location,
                          details=details)

        x.save()
        history = StudentComplain.objects.filter(complainer=y).order_by('-id')
        return render(request, "complaintModule/complaint_user.html", {'history': history, 'comp_id': comp_id})

    else:
        y = ExtraInfo.objects.get(id=comp_id)
        history = StudentComplain.objects.filter(complainer=y).order_by('-id')
        return render(request, "complaintModule/complaint_user.html", {'history': history, 'comp_id': comp_id})


def save_comp(request,comp_id1):
    if request.method == 'POST':
        comp_id = request.POST.get('comp_id', '')
        comp_type = request.POST.get('complaint_type', '')
        location = request.POST.get('Location', '')
        specific_location = request.POST.get('specific_location', '')
        details = request.POST.get('details', '')

        y = ExtraInfo.objects.get(id=comp_id)
        x=StudentComplain(complainer=y,
                          complaint_type=comp_type,
                          location=location,
                          specific_location=specific_location,
                          details=details)

        x.save()
        return HttpResponseRedirect('/complaint/user/'+comp_id)


def caretaker(request, comp_id):
    if request.method == 'POST':
        comp_type = request.POST.get('complaint_type', '')
        location = request.POST.get('Location', '')
        specific_location = request.POST.get('specific_location', '')
        details = request.POST.get('details', '')

        y=ExtraInfo.objects.get(id=comp_id)
        x=StudentComplain(complainer=y,
                          complaint_type=comp_type,
                          location=location,
                          specific_location=specific_location,
                          details=details)

        x.save()

        history = StudentComplain.objects.filter()
        return render(request, "complaintModule/complaint_caretaker.html", {'history': history})

    else:
        history = StudentComplain.objects.order_by('-id')
        return render(request, "complaintModule/complaint_caretaker.html", {'history': history})
