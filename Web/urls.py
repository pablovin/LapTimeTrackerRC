from django.urls import path

from . import views

app_name = "Web"
urlpatterns = [
    path('', views.index, name='index'),
    path('startSession', views.startSession, name='startSession'),
    path('stopSession', views.stopSession, name='stopSession'),
    path('updateSession', views.updateSession, name='updateSession')
]