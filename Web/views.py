from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings

import threading
import ctypes
import time
from Web.LapTracker.lapTracker import LapTracker

# Create your views here.


def index(request):
    return render(request, 'Web/index.html')

def startSession(request):

    settings.STOP_THREAD = False

    carName = request.POST.get('carName', False);
    trackDistance = request.POST.get('trackDistance', False);

    threadCamera = LapTracker(carName=carName,trackDistance=trackDistance)
    threadCamera.start()

    context = {'carName': carName, "trackDistance": trackDistance}

    # Update session
    session = {'carName': carName, "trackDistance": trackDistance}

    request.session['LTRCWeb'] = session


    return render(request, 'Web/timeTracker.html', context)


def updateSession(request):

    context = {'carName': "", "trackDistance": ""}

    return render(request, 'Web/timeTracker.html', context)


def stopSession(request):

    settings.STOP_THREAD = True


    context = {'carName': ""}
    return render(request, 'Web/index.html', context)