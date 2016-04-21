from django.conf.urls import url,include
from . import views

app_name = 'centerpiece'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^world/$', views.world_top, name='world'),
    url(r'^middleeast/$', views.middle_east_top, name='middleeast'),
    url(r'^europe/$', views.europe_top, name='europe'),
    url(r'^asia/$', views.asia_top, name='asia'),
    url(r'^usa/$', views.usa_top, name='usa'),
    url(r'^africa/$', views.africa_top, name='africa'),
	
]
