from django.shortcuts import render
from time import mktime, strftime, localtime, gmtime

def index(request):
    context = {
        # two different date/time formats, date and time
        "dateTime" : strftime("%B-%d-%Y", localtime()),
        "time" : strftime("%H:%M %p", localtime())
    }
    return render(request, "index.html", context)


