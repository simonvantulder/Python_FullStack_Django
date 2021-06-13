from django.urls import path
from . import views

# use restful routing
urlpatterns = [
    path('', views.index),# path in quotes and method name after views (in this case method = index)
    path('dojos/new', views.createDojo), # create new dojo path
    path('dojos/delete', views.deleteDojo), # delete a dojo path
    path('ninjas/new', views.createNinja), # create new ninja
]

# Book.objects.all().count()
