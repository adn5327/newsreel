from django.conf import urls
from . import views

app_name = 'centerpiece'
urlpatterns = [
    url(r'^$', views.index, name='index'),

]
