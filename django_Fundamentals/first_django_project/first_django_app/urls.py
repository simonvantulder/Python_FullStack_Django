
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:num>', views.show),
    path('blogs/<int:num>/edit', views.edit),
    path('blogs/<int:num>/destroy', views.destroy),
    path('blogs/json', views.jason),
]
