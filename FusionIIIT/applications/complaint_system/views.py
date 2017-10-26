from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentComplain
from applications.globals.models import ExtraInfo, User


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

def check(request):
    return HttpResponse("SUCESSFULL submission of data")
