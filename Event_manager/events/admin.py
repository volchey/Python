from django.contrib import admin
from .models import Location, Customer, Coordinator, Subject, TargetAudience, Event

admin.site.register(Location)
admin.site.register(Customer)
admin.site.register(Coordinator)
admin.site.register(Subject)
admin.site.register(TargetAudience)
admin.site.register(Event)
