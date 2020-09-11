from django.db import models

class Track(models.Model):

    name = models.CharField(max_length=200)
    lenght = models.IntegerField(default=0)

class Car(models.Model):
    name = models.CharField(max_length=200, default="Car")

class TrainingSession(models.Model):
    date = models.DateTimeField('Date', auto_now_add=True)

    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

class TrainingSessionDetails(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    date = models.DateTimeField('Date', auto_now_add=True)
    lapNumber = models.IntegerField(default=0)
    lapTime = models.FloatField(default=0)
    speed = models.IntegerField(default=0)

# Create your models here.
