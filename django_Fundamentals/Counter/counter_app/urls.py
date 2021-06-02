from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),	   
    path('index', views.index),	   
    path('index2', views.index2),	   
    path('destroy_session', views.destroy),	   
]