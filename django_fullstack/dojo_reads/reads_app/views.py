from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *

def index(request):
    return render (request, "login_index.html")


def user_create(request):
    errors = User.objects.validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hash_browns = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            name = request.POST["name"],
            alias = request.POST["alias"],
            birthday = request.POST["birthday"],
            email = request.POST["email"],
            password = hash_browns,
            )
        request.session['uuid'] = user.id

    return redirect ("/books")


def user_page(request, id):
    if 'uuid' not in request.session:
        return redirect("/")
    this_user = User.objects.get(id = id)
    context = {
        "user" : User.objects.get(id = id),
    }
    return render (request, "user_page.html", context)


def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user_list = User.objects.filter(email = request.POST['email'])
        user = user_list[0]
        request.session['uuid'] = user.id 

    return redirect("/books")


def books(request):
    if 'uuid' not in request.session:
        return redirect("/")

    else:
        this_user = User.objects.get(id = request.session['uuid'])
        context = {
            'books': Book.objects.all(),
            'reviews': Review.objects.all(),
            'user': this_user,

        }
        return render (request, "books.html", context)


def books_add(request):
    if 'uuid' not in request.session:
        return redirect("/")

    return render(request, "books_add.html")


def books_create(request):
    Book.objects.create(
        title = request.POST["title"],
        writer = request.POST["new_author"],
    )
    num = Book.objects.last()

    Author.objects.create(
        name = request.POST["new_author"],#how do i make this work if submitting from dropdown
    ) #preceding if statement? to check dropbown vs manual entry
    
    return redirect(f"/books/{num.id}")


def books_page(request, id):
    if 'uuid' not in request.session:
        return redirect("/")

    context = {
        'book': Book.objects.get(id=id),
        'reviews': Review.objects.filter(book=id),
        'users': User.objects.get(id = request.session['uuid']),

    }

    return render(request, "books_page.html", context)


def review_create(request):
    if 'uuid' not in request.session:
        return redirect("/")

    #person = User.objects.get(id = request.session["uuid"])
    Review.objects.create(
        users = User.objects.get(id = request.session["uuid"]),
        book = Book.objects.get(id = request.POST["bookID"]),
        content = request.POST["content"],
        rating = request.POST["rating"]

    )
    num = Book.objects.last()

    return redirect("/books")


def like_create(request, id):
    if 'uuid' not in request.session:
        return redirect("/")

    this_user = User.objects.get(id=request.session["uuid"])
    this_like = Review.objects.get(id=id)
    this_user.likes.add(this_like)

    return redirect("/books")


def logout(request):
    # print("breaks in logout")
    del request.session['uuid']
    
    return redirect("/")

def delete_review(request, id):

    this_review = Review.objects.get(id = id)
    this_review.delete()
    return redirect("/books")


def delete_book(request, id):

    this_book = Book.objects.get(id = id)
    this_book.delete()
    return redirect("/books")