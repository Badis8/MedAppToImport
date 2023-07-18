from django.db import models
from  django.contrib.auth.models import User
class Medicament(models.Model):
    id = models.CharField(primary_key=True,max_length=1000)
    name = models.CharField(max_length=255)
    prixPublic=models.FloatField()
    list=models.CharField(max_length=1)
    def __str__(self):
        return str(self.id)
    
class Ordonnance(models.Model):
    id = models.AutoField(primary_key=True)
    usernameDestination=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_Destination")
    Doctor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Doctor_Destination")
    etat=models.CharField(max_length=255)
    decision=models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class LigneOrdonnance(models.Model):
    id = models.AutoField(primary_key=True)
    Medicament = models.ForeignKey(Medicament,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    qauntityPerDay=models.DecimalField(max_digits=10, decimal_places=2)
    remarks=models.CharField(max_length=1255)
    Ordonnance=models.ForeignKey(Ordonnance,on_delete=models.CASCADE,related_name="ligne")
    def __str__(self):
        return str(self.id)
class PharmacistPendingOrdoannance(models.Model):
    Pharmaciste=models.ForeignKey(User,on_delete=models.CASCADE,related_name="PendingOrdonnancePhrmacist")
    Ordonnance=models.ForeignKey(Ordonnance,on_delete=models.CASCADE,related_name="PharmacistOrdonnance")  
    
    def __str__(self):
        return str(self.id)
class UserPendingOrdoannance(models.Model):
    userWaiting=models.ForeignKey(User,on_delete=models.CASCADE,related_name="PendingOrdonnancePatient")
    Ordonnance=models.ForeignKey(Ordonnance,on_delete=models.CASCADE,related_name="UsersWaiting")
    def __str__(self):
        return str(self.id)

# Create your models here.
 