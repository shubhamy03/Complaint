from django.conf.urls import url

from . import views

app_name = 'complaint'

urlpatterns = [

    # url(r'^user/(?P<comp_id>[0-9]+)$', views.complaint, name='complaint'),
    url(r'^user/(?P<comp_id>[0-9]+)/$', views.user, name='complaint'),
    url(r'^user/(?P<comp_id1>[0-9]+)/check_complaint/$', views.save_comp, name='complaint'),
    # url(r'^temp_complaint_sub/', views.temp_complaint_sub, name='complaint'),
    url(r'^caretaker/(?P<comp_id>[0-9]+)$', views.caretaker, name='complaint'),
    url(r'^home/(?P<comp_id>[0-9]+)/$', views.assign_worker),
    url(r'^check/$', views.check, name='complaint'),

]
