from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),# path in quotes and method name after views (in this case method = index)
    path('shows', views.shows),# path in quotes and method name after views (in this case method = index)
    path('shows/new', views.add_show),
    path('shows/create', views.create_show),
    path('shows/<int:num>/edit', views.edit_show),
    path('shows/<int:num>/update', views.update_show),
    path('show/<int:num>', views.show),
    path('shows/<int:num>/delete', views.delete_show),

]

