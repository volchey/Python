from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import EventCreate

urlpatterns = [
    url(r'^$', views.calendar, name='calendar'),
    url(r'^create-event/$', EventCreate.as_view(), name='create-event'),
]

admin.site.site_header = 'Event Manager administration'