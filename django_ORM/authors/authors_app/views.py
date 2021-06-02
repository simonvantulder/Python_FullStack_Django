from django.shortcuts import render, redirect
from . models import *


def books_index(request):
    context = {
        "books": Book.objects.all(), #returns a list of every dojo in DB
    }    
    return render(request, "index.html", context)

def book(request, num):
    this_book = Book.objects.get(id=num)
    context = {
        "book": Book.objects.get(id=num), #returns a specific instance of the book class in DB
        "authors": Author.objects.all(), #returns a list of every author in DB
        "writers": this_book.authors.all(),
    }    
    return render(request, "book.html",context)

def books_create(request):
    Book.objects.create(
        title = request.POST["title"],
        desc = request.POST["description"],
        )
    return redirect("/")

def book_add_author(request):
    this_author = Author.objects.get(id=request.POST["Author_id"])
    this_book = Book.objects.get(id=request.POST["ID"])
    this_author.books.add(this_book)

    return redirect(f"/books/{request.POST['ID']}")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def authors_index(request):
    context = {
        "authors": Author.objects.all(), #returns a list of every author in DB
    }    
    return render(request, "authors_index.html", context)

def author(request, num):
    this_author = Author.objects.get(id = num)
    context = {
        "author": Author.objects.get(id = num), #returns a specific instance of author class in DB
        "books": Book.objects.all(), #returns a specific instance of the book class in DB
        "writings":this_author.books.all()
    }    
    return render(request, "author.html", context)

def authors_create(request):
    Author.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        text = request.POST["notes"],
        )
    return redirect("/authors")

def author_add_book(request):
    this_author = Author.objects.get(id= request.POST["ID"])
    this_book = Book.objects.get(id=request.POST["ISBN"])
    this_author.books.add(this_book)

    return redirect(f"/authors/{request.POST['ID']}")
