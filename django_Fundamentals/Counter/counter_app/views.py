

from django.shortcuts import render, HttpResponse, redirect

def root(request):
    # request.session['name'] = request.POST['name']
    if 'pageCounter' in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] = 0
        request.session['pageCounter'] = 0

    return redirect("/index")
def index(request):
    request.session['counter'] += 1
    request.session['pageCounter'] +=1
    return render(request, "index.html")
def index2(request):
    request.session['counter'] += 1
    return redirect("/index")
def destroy(request):
    del request.session['counter']
    return redirect("/")
