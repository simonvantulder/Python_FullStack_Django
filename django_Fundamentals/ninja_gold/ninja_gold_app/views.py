from django.shortcuts import render, redirect
import random

def index(request):
    if "gold_count" in request.session: # display the amount of gold a user has if they have started the game
        print(request.session["gold_count"])
        request.session["winner"] = False
        if "attempts" in request.session:
            request.session['attempts'] +=1

    else:
        request.session["attempts"] = 0 #else display the defaults
        request.session["gold_count"]=10
        request.session["activities"]=[]

    return render(request,"index.html")

def process(request): # depending on the activity selected by the user, display the resulting gold earned/lost
    if request.POST['box'] =='farm':
        gold_gained = random.randint(10,20)
        request.session['gold_count'] += gold_gained
        request.session["activities"].append("Earned {} gold from the farm!".format(gold_gained))
        print(request.session["activities"])

    if request.POST['box'] == 'cave':
        mined = random.randint(5, 10)
        request.session['gold_count'] += mined
        request.session["activities"].append("Earned {} gold from the cave!".format(mined))

    elif request.POST['box'] =='house':
        gold_from_couch_pillows = random.randint(2, 5)
        request.session['gold_count'] += gold_from_couch_pillows
        request.session["activities"].append("Found {} gold in the couch cushions!".format(gold_from_couch_pillows))

    else:
        bet = random.randint(-50, 50)
        request.session['gold_count'] += bet
        if(bet > 0):
            request.session["activities"].append("won {} gold from the casino!".format(bet))
        else:
            request.session["activities"].append("lost {} gold from the casino".format(bet))
        
    # delete the last entry to prevent stack overflow
    if len(request.session["activities"])>5:
        request.session["activities"].reverse()
        request.session["activities"].pop()    
        request.session["activities"].reverse()    

    return redirect("/")

def reset(request): # display gold & attempts
    request.session["gold_count"]=10
    request.session["attempts"] = 0
    return redirect("/")