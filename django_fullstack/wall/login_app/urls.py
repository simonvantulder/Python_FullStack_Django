from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),# path in quotes and method name after views (in this case method = index)
    path('user/login', views.index),# path in quotes and method name after views (in this case method = index)
    path('login/user/register', views.user_create),
    path('login', views.login),
    path('logout', views.logout),

]