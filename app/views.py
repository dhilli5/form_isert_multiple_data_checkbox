from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import  Games,Player,Location

def insert_games(request):
    if request.method=="POST":
        gn=request.POST["game"]
        GO=Games.objects.get_or_create(game_n=gn)[0]
        GO.save()
        return HttpResponse("insert game data successfully")
    return render(request,'insert_games.html')

def insert_player(request):  # sourcery skip: extract-method
    if request.method=="POST":
        gn=request.POST["gamess"]
        
        GO=Games.objects.get(game_n=gn)
        GO.save()
        pn=request.POST["pn1"]
        age=request.POST["pa1"]
        PO=Player.objects.get_or_create(game_n=GO,player_n=pn,age=age)[0]
        PO.save()
        return HttpResponse("player data insert successfully")
    LOG=Games.objects.all()
    d={"game":LOG}
    return render(request,"insert_player.html",context=d)
def insert_location(request): # sourcery skip: extract-method
    if request.method=="POST":
        pn=request.POST["play"]
        
        PO=Player.objects.get(player_n=pn)
        PO.save()
        ci=request.POST["ci1"]
        st=request.POST["st1"]
        LO=Location.objects.get_or_create(player_n=PO,city=ci,state=st)[0]
        LO.save()
        return HttpResponse("player data insert successfully")
    LOL=Player.objects.all()
    d={"play":LOL}
    return render(request,"insert_location.html",context=d)

def retrieve_data(request): # sourcery skip: extract-method
    LOG=Games.objects.all()
    d={"games":LOG}
    if request.method=="POST":
        gn=request.POST.getlist('games')
        print(gn)
        webqueryset=Player.objects.none()
        
        
        for i in gn:
            webqueryset=webqueryset|Player.objects.filter(game_n=i)
        d1={'players':webqueryset}
        return render(request,'display_player.html',d1)
    return render(request,'retrieve_data.html',d)
def display_player(request):

    return render(request,'display_player.html')

def checkbox(request):
    LTO=Games.objects.all()
    d2={'games':LTO}
    return render(request,'checkbox.html',d2)


    

def retrieve_data_player(request):  # sourcery skip: extract-method
    LOP=Player.objects.all()
    d={"players":LOP}
    if request.method=="POST":
        pn=request.POST.getlist('players')
        print(pn)
        webqueryset=Location.objects.none()
        
        for x in pn:
            webqueryset=webqueryset|Location.objects.filter(player_n=x)
        print(webqueryset)
        d1={'locations':webqueryset}
        return render(request,'display_location.html',d1)
    return render(request,'retrieve_data_player.html',d)

def display_location(request):
    
    return render(request,"display_location.html")

def checkbox_player(request):
    LTO=Player.objects.all()
    d2={'players':LTO}
    return render(request,'checkbox_player.html',d2)
    

def radio(request):
    LTO=Games.objects.all()
    d3={"games":LTO}
    
    return render(request,'radio.html',d3)



def updating_data(request):
    if request.method=="POST":
        gn=request.POST["game"]
        pn=request.POST["player"]
        Player.objects.filter(game_n=gn).update(player_n=pn)
        d1={"players":Player.objects.all()}
        return render(request,'display_player.html',d1)
    
    return render(request,'updating_data.html')

