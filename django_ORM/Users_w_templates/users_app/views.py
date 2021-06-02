from django.shortcuts import render, HttpResponse, redirect
from . models import Users #import Users or use * to import everything from .models 

def index(request):
    context = {
        "users": Users.objects.all() #returns a list of everything in DB
    }
    return render(request, "index.html", context)

def create(request):
    Users.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        email_address = request.POST["email"],
        age = request.POST["age"],
    )

    return redirect("/")