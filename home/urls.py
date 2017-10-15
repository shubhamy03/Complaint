from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views
app_name = 'home'


urlpatterns = [
    url(r'^login/$',views.auth),
    url(r'^index/$', views.index, name='index'),
    url(r'^home/$', views.index1, name='index1'),
    url(r'^compl_form/$', views.compl_form, name='login'),
#    url(r'^show_data/(?P<cate>[-\w]+)/$', views.show_data, name='show_data'),
    url(r'^show_data/(?P<comp_id>[0-9]+)/$', views.show_data, name='show_data'),
#    url(r'^check/', views.auth),



    url(r'^complaint_details/(?P<comp_id>[0-9]+)/$', views.complaint_details, name='show_data'),

#    url(r'^check_care/$',views.check_cares)


]
