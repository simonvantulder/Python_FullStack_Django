from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('user/register', views.user_create),
    path('user/<int:id>', views.user_page),
    path('login', views.login),
    path('books', views.books),
    path('books/add', views.books_add),
    path('books/create', views.books_create),
    path('books/<int:id>', views.books_page),
    path('book/<int:id>/delete', views.delete_book),
    path('review/create', views.review_create),
    path('review/<int:id>/delete', views.delete_review),
    path('like/<int:id>', views.like_create),

    path('logout', views.logout),

]