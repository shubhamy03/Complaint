from django import forms
from .models import StudentComplain

#class omplaint_form(forms.Form):
#    com_id = forms.CharField(label='com_id',max_length=10)
#    location = forms.CharField(label='location',max_length=20)
#     details = forms.CharField(label='details',max_length=100)

class complain_form(forms.ModelForm):
    class Meta:
        model=StudentComplain
        fields={'location','specific_location','details'}

class login_form(forms.Form):
    userid=forms.CharField(max_length=8)

