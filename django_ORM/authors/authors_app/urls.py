from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_index),# path in quotes and method name after views (in this case method = index)
    path('books/create', views.books_create),# path in quotes and method name after views (in this case method = index)
    path('books/<int:num>', views.book),# path in quotes and method name after views (in this case method = index)
    path('books/add/author', views.book_add_author),# path in quotes and method name after views (in this case method = index)
    path('authors', views.authors_index),# path in quotes and method name after views (in this case method = index)
    path('authors/create', views.authors_create),# path in quotes and method name after views (in this case method = index)
    path('authors/<int:num>', views.author),# path in quotes and method name after views (in this case method = index)
    path('authors/add/book', views.author_add_book),# path in quotes and method name after views (in this case method = index)
]


