from django.urls import path

from . import views

app_name = "Web"
urlpatterns = [
    path('', views.index, name='index'),
    path("index", views.index, name='index'),
    path('addCar', views.addCar, name='addCar'),
    path('addTrack', views.addTrack, name='addTrack'),
    path('startSession', views.startSession, name='startSession'),
    path('stopSession', views.stopSession, name='stopSession'),
    path('updateSession', views.updateSession, name='updateSession')
]