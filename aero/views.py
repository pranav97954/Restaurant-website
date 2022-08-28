from django.shortcuts import render
from aero.models import *
from django.http import HttpResponseRedirect,HttpResponse

def home(request):
    res=render(request,'HTML/home.html')
    return res

def order(request):
    res=render(request,'HTML/order.html')
    return res

def menu(request):
    res=render(request,'HTML/menu.html')
    return res

def cart(request):
    res=render(request,'HTML/cart.html')
    return res

def reservation(request):
    res=render(request,'HTML/Reservation.html')
    return res

def parties(request):
    res=render(request,'HTML/Parties.html')
    return res
 
def contact(request):
    res=render(request,'HTML/contactus.html')
    return res

def contactus_save(request):
    cont=contactus()
    cont.firstname=request.POST['fname']
    cont.lastname=request.POST['lname']
    cont.phonenumber=request.POST['pnumber']
    cont.emails=request.POST['email']
    cont.messages=request.POST['message']
    cont.save()
    res=render(request,'HTML/home.html')
    return res
    
def viewcontactus(request):
    cont=contactus.objects.all()
    res=render(request,'HTML/viewcontactus.html',{'cont':cont})
    return res
    
def parties_save(request):
    part=partiescontact()
    part.name=request.POST['Name']
    part.numofguest=request.POST['numberofguest']
    part.evname=request.POST['eventname']
    part.da=request.POST['date']
    part.startti=request.POST['starttime']
    part.endti=request.POST['endtime']
    part.pnumber=request.POST['Pnumber']
    part.emails2=request.POST['email1']
    part.messages2=request.POST['Messagesforparty']
    part.save()
    res=render(request,'HTML/home.html')
    return res

def ViewPartiesContact(request):
    part=partiescontact.objects.all()
    res=render(request,'HTML/viewpartiescontact.html',{'part':part})
    return res

    


