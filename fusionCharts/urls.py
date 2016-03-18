from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.demo,  name='demo'),
    url(r'^event/', views.event, name='event'),
    url(r'^xml/', views.xml, name='xml'),
]
