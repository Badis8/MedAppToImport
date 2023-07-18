from django.db import models
from  django.contrib.auth.models import User
class PendingDoctors(models.Model):
    username=models.CharField("username",max_length=50)
    First_name=models.CharField("First_name",max_length=50)
    Last_name=models.CharField("Last_name",max_length=50)
    Email=models.EmailField("email")
    Specialty=models.CharField("Specialty",max_length=50)
    address=models.CharField("address",max_length=50)
    phoneNumber=models.CharField("phone number",max_length=8)
    password=models.CharField("password",max_length=100)
    def __str__(self):
        return self.username

class PendingPharmacists(models.Model):
    username=models.CharField("username",max_length=50)
    First_name=models.CharField("First_name",max_length=50)
    Last_name=models.CharField("Last_name",max_length=50)
    Email=models.EmailField("email")
    address=models.CharField("address",max_length=50)
    phoneNumber=models.CharField("phone number",max_length=8)
    password=models.CharField("password",max_length=100)
    def __str__(self):
        return self.username

class actualDoctors(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="doctors")
    Specialty=models.CharField("Specialty",max_length=50)
    address=models.CharField("address",max_length=50)
    phoneNumber=models.CharField("phone number",max_length=8)
    def __str__(self):
        return self.username.username
class actualPharmacist(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name="pharmacists")
    address=models.CharField("address",max_length=50)
    phoneNumber=models.CharField("phone number",max_length=8)
    def __str__(self):
        return self.username.username

# Create your models here.
