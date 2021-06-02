from django.shortcuts import render, HttpResponse
def index(request):

    return render(request,"index.html")

def process(request):
    print(request.POST)

    instructors_survey=[]#create empty list and add on line 13-16
    name_from_survey =request.POST["name1"]
    location_survey = request.POST["location"]#pulling data from the post request
    language_survey = request.POST["language"]
    if "instructor1" in request.POST:
        instructors_survey.append(request.POST["instructor1"])
    if "instructor2" in request.POST:
        instructors_survey.append(request.POST["instructor2"])
    activity_survey =request.POST["activity"]
    comment_survey =request.POST["comment"]
    context = {
        "name_template" : name_from_survey,
        "location_template" :location_survey,
        "language_template" : language_survey,
        "instructors_template": instructors_survey,#this is now a list. only this one
        "activity_template": activity_survey,
        "comment_template":comment_survey
    }
    print(instructors_survey)#i think this can be commented out now...havent bothered to check

    return render(request, "show.html", context)#three items max: request, html to be rendered & one (optional) dictionary 
    
