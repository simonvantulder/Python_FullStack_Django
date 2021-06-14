from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("I will code 500 lines...")

def new(request):
    return HttpResponse("...and I will code 500 more")

def create (request):
    return redirect("/")

def show (request, num):
    return HttpResponse(f"to be the man who codes {num} lines to fix your app")

def edit (request, num):
    return HttpResponse(f"to be the man to edit {num} lines of code to fix your app")

def destroy (request,num):
    return redirect("/blogs")

def jason (request):
    return JsonResponse({'title':'"my first blog",', 'content':  '"Lorem ipsum dolor sit amet consectetur adipisicing elit."' })