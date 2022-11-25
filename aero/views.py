import email
from django.shortcuts import redirect, render
from aero.models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    res=render(request,'HTML/index.html')
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
    res=render(request,'HTML/index.html')
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
    res=render(request,'HTML/index.html')
    return res

def ViewPartiesContact(request):
    part=partiescontact.objects.all()
    res=render(request,'HTML/viewpartiescontact.html',{'part':part})
    return res

def login(request):
    res=render(request,'HTML/login.html')  
    return res  

def signup(request):
 
    if request.method == "POST":
        #username = username.POST.get('username')
        #firstname = firstname.POST.get('firstname')
        #lastname = lastname.POST.get('lastname')
        #emailid = emailid.POST.get('emailid')
        #pass1 = pass1.POST.get('pass1')
        #pass2 = pass2.POST.get('pass2')
        conta= signinuser()
        conta.username = request.POST['username']
        conta.firstname = request.POST['firstname']
        conta.lastname = request.POST['lastname']
        conta.emailid = request.POST['emailid']
        conta.pass1 = request.POST['pass1']
        conta.pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,emailid,pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()

        messages.success(request,"Your Account has been created Successfully")
        return redirect('http://localhost:8000/aero/login/')

    res=render(request,'HTML/signup.html')
    return res

def signout(request):
    pass


