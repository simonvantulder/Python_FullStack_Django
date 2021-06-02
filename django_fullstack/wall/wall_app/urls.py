from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('dashboard', views.dashboard),
    path('message/new', views.create_message),
    path('wall', views.wall),
    path('comment/new', views.create_comment),

]