from django.db import models

class contactus(models.Model):
    number=models.IntegerField(primary_key=True,auto_created=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phonenumber=models.IntegerField()
    emails=models.CharField(max_length=40)
    messages=models.CharField(max_length=300)
    
class partiescontact(models.Model):
    number=models.IntegerField(primary_key=True,auto_created=True)
    name=models.CharField(max_length=60)
    numofguest=models.IntegerField()
    evname=models.CharField(max_length=20)
    da=models.DateField()
    startti=models.TimeField()
    endti=models.TimeField()
    pnumber=models.IntegerField()
    emails2=models.CharField(max_length=40)
    messages2=models.CharField(max_length=300)