from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_games(request):
    if request.method=="POST":
        gn=request.POST["game"]
        GO=Games.objects.get_or_create(gamen=gn)[0]
        GO.save()
        return HttpResponse("insert game data successfully")
    return render(request,'insert_games.html')
def insert_player(request):
    if request.method=="POST":
        gn=request.POST["game"]
        GO=Games.objects.get(gamen=gn)
        GO.save()
       
        
        pn=request.POST["pn1"]
        age=request.POST["pa1"]
       
        PO=Player.objects.get_or_create(gamen=GO,playern=pn,age=age)[0]
        PO.save()
        return HttpResponse("player data insert successfully")
    LOG=Games.objects.all()
    d={"game":LOG}
   
    return render(request,"insert_player.html",context=d)
def insert_location(request):
    if request.method=="POST":
        pn=request.POST["play"]
        PO=Player.objects.get(playern=pn)
        PO.save()
       
        
        ci=request.POST["ci1"]
        st=request.POST["st1"]
       
        LO=Location.objects.get_or_create(playern=PO,city=ci,state=st)[0]
        LO.save()
        return HttpResponse("player data insert successfully")
    LOL=Player.objects.all()
    d={"play":LOL}
   
    return render(request,"insert_location.html",context=d)
