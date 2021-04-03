from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^create-event/$', views.create_event, name='create-event'),
]