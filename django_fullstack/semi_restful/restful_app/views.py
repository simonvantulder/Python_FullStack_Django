from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *


# display main page
def index(request):
    context = {
        "shows": Show.objects.all(), #returns a list of every tv show in DB
    }
    return redirect("/shows")


# display all the tv shows in DB
def shows(request):
    context = {
        "shows": Show.objects.all(), #returns a list of every tv show in DB
    }
    return render(request, "index.html", context)


# display tv show creation form/page
def add_show(request):

    return render(request, "new_show.html")


# handle tv show creation
def create_show(request):
    errors = Show.objects.validator(request.POST)
    print(request.POST["release_date"])
    print("test")
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/shows/new')
    else:
        Show.objects.create(
            title = request.POST["title"],
            network = request.POST["network"],
            release_date = request.POST["release_date"],
            desc = request.POST["description"],
            )
        num = Show.objects.last()
    return redirect(f"/show/{num.id}")


# display edit page for tv show
def edit_show(request, num):
    context = {
        "show": Show.objects.get(id = num)
    }
    return render(request, "edit_show.html", context)


# handle tv show update
def update_show(request, num):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/shows/{num}/edit')
    else:
        this_show = Show.objects.get(id = num)
        this_show.title = request.POST["title"]
        this_show.network = request.POST["network"]
        this_show.release_date = request.POST["release_date"]
        this_show.desc = request.POST["description"]
        this_show.save()

    return redirect(f"/show/{num}")# change to redirect to the specific show


# display single tv show
def show(request, num):
    context = {
        "show": Show.objects.get(id = num), #returns a specific instance of the show class in DB
    }    
    return render(request, "show.html", context)


# remove tv show from database
def delete_show(request, num):
    this_show = Show.objects.get(id = num)
    this_show.delete()

    return redirect("/")


