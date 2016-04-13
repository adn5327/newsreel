from django.conf.urls import url,include
from . import views

app_name = 'centerpiece'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^world/$', views.world_top, name='world'),
    url(r'^africa/$', views.africa_top, name='africa'),
]
