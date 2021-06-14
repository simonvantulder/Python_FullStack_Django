from django.shortcuts import render, HttpResponse, redirect

# set counter if not in session
def root(request):
    if 'pageCounter' in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] = 0
        request.session['pageCounter'] = 0

    return redirect("/index")


# increment counter & page counterfor each time page is visited/reloaded
def pageCount(request):
    request.session['counter'] += 1
    request.session['pageCounter'] +=1
    return render(request, "index.html")


# increment only the counter not the page counter for each time button is clicked
def count(request):
    request.session['counter'] += 1

    return redirect("/index")


# reset counter
def destroy(request):
    del request.session['counter']

    return redirect("/")
