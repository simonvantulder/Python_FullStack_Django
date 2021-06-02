from django.shortcuts import render, HttpResponse, redirect
from . models import *


def index(request):
    context = {
        "dojos": Dojo.objects.all(), #returns a list of every dojo in DB
    }
    return render(request, "index.html", context)

def createNinja(request):
    Ninja.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        dojo_ID = Dojo.objects.get(id=request.POST["dojo_id"]),
    )
    return redirect("/")

def createDojo(request):
    Dojo.objects.create(
        name = request.POST["name"],
        city = request.POST["city"],
        state = request.POST["state"],
    )
    return redirect("/")

def deleteDojo(request):
    Dojo.objects.get(id=request.POST["delete_id"]).ninjas.all().delete()
    Dojo.objects.get(id=request.POST["delete_id"]).delete()

    return redirect("/")