from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.shortcuts import redirect

import threading
import ctypes
import time
from Web.LapTracker.lapTracker import LapTracker

from Web.models import Track, Car
# Create your views here.

def loadCarsAndTracks():

    tracks = []
    for t in Track.objects.all():
        tracks.append(t.name)

    cars = []
    for t in Car.objects.all():
        cars.append(t.name)

    return tracks, cars

def index(request):

    tracks,cars = loadCarsAndTracks()

    context = {'tracks': tracks, "cars": cars}

    return render(request, 'Web/index.html', context)


def addCar(request):
    carName = request.POST.get('newCarNameID', False);

    newCar = Car(name=carName)
    newCar.save()

    tracks, cars = loadCarsAndTracks()

    context = {'tracks': tracks, "cars": cars}

    return render(request, 'Web/index.html', context)

def addTrack(request):
    trackName = request.POST.get('newTrackNameID', False);
    trackLength = request.POST.get('newTrackLenghtID', False);

    newTrack = Track(name=trackName, length=trackLength)
    newTrack.save()

    tracks, cars = loadCarsAndTracks()

    context = {'tracks': tracks, "cars": cars}

    return render(request, 'Web/index.html', context)


def startSession(request):

    settings.STOP_THREAD = False
    carName = request.POST['selectedCarID']
    trackName = request.POST['selectedTrackNameID']


    car = Car.objects.get(name=carName)
    track = Track.objects.get(name=trackName)

    threadCamera = LapTracker(car=car,track=track)
    threadCamera.start()

    context = {'carName': car.name, "trackDistance": track.lenght}

    # Update session
    session = {'carName': car.name, "trackDistance": track.lenght}

    request.session['LTRCWeb'] = session


    return render(request, 'Web/timeTracker.html', context)


def updateSession(request):

    context = {'carName': "", "trackDistance": ""}

    return render(request, 'Web/timeTracker.html', context)


def stopSession(request):

    settings.STOP_THREAD = True

    context = {'carName': ""}
    return render(request, 'Web/index.html', context)


def cameraConfig():
    return None