from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *


# display main page
def dashboard(request):
    if 'uuid' not in request.session:
        return redirect("/")

    else:
        this_user = User.objects.get(id = request.session['uuid'])
        context = {
            'messages': Message.objects.all(),
        }
        return render (request, "index.html", context)


# imitation fb wall, get user and all messages to display
def wall(request):
    if 'uuid' not in request.session:
        return redirect("/")

    else:
        context = {
            'user': User.objects.get(id = request.session['uuid']),
            'messages': Message.objects.all().order_by("-created_at"),
        }
        return render (request, "wall.html", context)


# handle method creation
def create_message(request):
    if 'uuid' not in request.session:
        return redirect("/")

    else:
        this_user = User.objects.get(id = request.session['uuid'])

    Message.objects.create(
        person = this_user,
        content = request.POST["content"],
    )
    return redirect("/dashboard")


# handle comment creation
def create_comment(request):
    if 'uuid' not in request.session:
        return redirect("/")

    else:
        this_user = User.objects.get(id = request.session['uuid'])
        this_message = Message.objects.get(id = request.POST['post_id'])

    Comment.objects.create(

        person = this_user,
        post = this_message,
        content = request.POST["content"],
    )
    return redirect("/wall")

