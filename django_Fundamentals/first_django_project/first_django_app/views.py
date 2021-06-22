from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# redirect to main page
def root(request):
    return redirect("/blogs")


# display main page
def index(request):
    return HttpResponse("I will code 500 lines...")


# display different page
def new(request):
    return HttpResponse("...and I will code 500 more")


# redirect
def create (request):
    return redirect("/")


# practice ability to route to another page with a variable input
def show (request, num):
    return HttpResponse(f"to be the man who codes {num} lines to fix your app")


# practice ability to route to another page with a variable input
def edit (request, num):
    return HttpResponse(f"to be the man to edit {num} lines of code to fix your app")


# prep page for item deletion
def destroy (request,num):
    return redirect("/blogs")


# practice Json response handling
def jason (request):
    return JsonResponse({'title':'"my first blog",', 'content':  '"Lorem ipsum dolor sit amet consectetur adipisicing elit."' })