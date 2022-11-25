from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('menu/',menu),
    path('order/',order),
    path('',home),
    path('reservation/',reservation),
    path('parties/',parties),
    path('contact/',contact),
    path('cart/',cart),
    path('savecontactus/',contactus_save),
    path('viewcontact/',viewcontactus),
    path('partiessave/',parties_save),
    path('ViewPartiesContact/',ViewPartiesContact),
    path('login/',login ,name="login"),
    path('signup/',signup,name="signup"),
    path('sigout/',signout,name="signout"),
]