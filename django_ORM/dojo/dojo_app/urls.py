from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),# path in quotes and method name after views (in this case method = index)
    path('dojos/new', views.createDojo),
    path('dojos/delete', views.deleteDojo),
    path('ninjas/new', views.createNinja),
]

# Book.objects.all().count()
