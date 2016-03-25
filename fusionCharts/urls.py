from django.conf.urls import url

from . import views
from . import staticJsonExample, staticXmlExample, dictExample, xmlDictExample, databaseExample, drilldownExample

urlpatterns = [
    url(r'^$', views.demo,  name='demo'),
    url(r'^event/', views.event, name='event'),
    url(r'^jsonurl/', views.jsonurl, name='jsonurl'),
    url(r'^xmlurl/', views.xmlurl, name='xmlurl'),

    url(r'^staticJsonExample/', staticJsonExample.fc_json, name='fc_json'),
    url(r'^staticXmlExample/', staticXmlExample.fc_xml, name='fc_xml'),
    url(r'^dictExample/', dictExample.fc_dict, name='fc_dict'),
    url(r'^xmlDictExample/', xmlDictExample.fc_xmldict, name='fc_dictxml'),
    url(r'^db/', databaseExample.fc_db, name='fc_db'),
    url(r'^drilldown/$', drilldownExample.fc_drilldown, name='fc_drilldown'),

]
