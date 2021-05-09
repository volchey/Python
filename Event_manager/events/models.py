from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)

    def __str__(self):
        return self.name

class Customer(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name + " " + self.surname

class Coordinator(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name + " " + self.surname

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500)
    color = ColorField(default='#c3e0a8')

    def __str__(self):
        return self.description

class TargetAudience(models.Model):
    description = models.CharField(max_length=500)
    agemin = models.IntegerField(default=18)
    agemax = models.IntegerField(default=60)

    def __str__(self):
        return self.description

class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    starttime = models.DateTimeField(default=None)
    endtime = models.DateTimeField(default=None)

    def __str__(self):
        return self.title