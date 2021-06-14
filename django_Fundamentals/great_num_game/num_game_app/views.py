from django.shortcuts import render, redirect
#  from random import random.randint
import random

def index(request):
    # process subsequent guesses 
    if "answer" in request.session:
        print(request.session["answer"]) # print answer in console
        request.session["Buttons"] = "Submit"
        request.session["winner"] = False
        if "attempts" in request.session:
            request.session['attempts'] +=1

# initialize for first guess
    else: 
        request.session["answer"] = random.randint(1, 100)
        request.session["attempts"] = 0
        request.session["hint"] = ""
        request.session["Buttons"] = "Submit"
        request.session["winner"] = False

        print(request.session["answer"])

    return render(request,"index.html")

# process guess, display hint: guess too high, too low or correct
def process(request):
    if "guess" in request.POST:
        form_guess = int(request.POST["guess"])
        if int(request.POST["guess"]) < request.session["answer"]:
            request.session["hint"] = "guess higher"
            return redirect("/")
        elif form_guess>request.session["answer"]:
            request.session["hint"] = "guess lower"
            return redirect("/")
        if int(request.POST["guess"])==request.session["answer"]:
            request.session["hint"] = "You got it!"
            request.session["winner"] = True
            request.session["Buttons"] = "Play Again?"
            return redirect("/reset")
        
    return redirect("/")

    #process the reset method to go again
def reset(request): 
    request.session['answer'] = random.randint(1, 100)
    request.session['attempts'] = 0 
    request.session["winner"] = False

    return redirect("/")
