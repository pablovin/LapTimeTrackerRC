from django.contrib import admin

from .models import Car, Track, TrainingSession, TrainingSessionDetails

admin.site.register(Car)
admin.site.register(Track)
admin.site.register(TrainingSession)
admin.site.register(TrainingSessionDetails)

# Register your models here.
