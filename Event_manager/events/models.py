from django.db import models
from django.utils import timezone

class Location(models.Model):
    # id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)

class Customer(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)

class Coordinator(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500)

class TargetAudience(models.Model):
    description = models.CharField(max_length=500)
    agemin = models.IntegerField(default=18)
    agemax = models.IntegerField(default=60)

class Event(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    color = models.IntegerField(default=13622955)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    starttime = models.DateTimeField(default=None)
    endtime = models.DateTimeField(default=None)

    def __str__(self):
        return self.title