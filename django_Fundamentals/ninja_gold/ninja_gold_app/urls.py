
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # start page
    path('process', views.process), # process activity
    path('reset', views.reset), # reset the game
]
