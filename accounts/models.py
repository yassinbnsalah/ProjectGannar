from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client (models.Model):
    nom = models.CharField(max_length=50, null = True) 
    prenom = models.CharField(max_length=50 , null = True) 
    email = models.CharField(max_length=250 , null = True) 
    is_employees = models.BooleanField(default= False , null = True)
    numero_tel = models.CharField(max_length = 8 ,null = True , default ="00000000")
    adress = models.CharField(max_length=250 , null = True , default= "unknow")
    user = models.ForeignKey(User , null = True , on_delete= models.CASCADE )
    def __str__(self):
        return self.nom

class Ouvrier (models.Model): 
    client = models.ForeignKey(Client , null = True , on_delete=models.CASCADE)
    job = models.CharField(max_length=50 , null = True)
    desponibility = models.CharField(max_length=50 , null = True)
    description = models.CharField(max_length = 250 , null = True)
    def __str__(self):
        return self.client.nom
    

class Demmande (models.Model):
    client = models.ForeignKey(Client , related_name="demande" ,null = True , on_delete= models.CASCADE)
    job = models.CharField(max_length= 50 , null = True )
    disponible = models.CharField(max_length=50 , null = True) 
    description = models.CharField(max_length= 250 , null = True )
    #def __str__(self):
     #   return self.client.nom

class Request_Role (models.Model):
    client = models.ForeignKey(Client , null = True , on_delete= models.CASCADE)
    demande = models.ForeignKey(Demmande , null = True , on_delete = models.CASCADE)