from django.shortcuts import render
from time import mktime, strftime, localtime, gmtime

def index(request):
    context = {
        # i dont know how this works...should pull localtime but still pulls meridian time
        "time" : strftime("%B-%d-%Y", localtime()),
        "time2" : strftime("%H:%M %p", localtime())
    }
    return render(request, "index.html", context)


