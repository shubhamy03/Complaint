from django.conf.urls import url

from . import views

app_name = 'complaint'

urlpatterns = [

    url(r'^', views.complaint, name='complaint'),
    # url(r'^temp_complaint_sub/', views.temp_complaint_sub, name='complaint'),

    #url(r'^check/', views.check),

]
