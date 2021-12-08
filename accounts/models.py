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
    is_requested = models.BooleanField(null = True , default = False)
    image = models.ImageField(upload_to='images' , null = True , default = "images/avatar-11.jpg")
    user = models.ForeignKey(User , null = True , on_delete= models.CASCADE )
    def __str__(self):
        return self.nom

class Categorie (models.Model):
    name = models.CharField(max_length=50 , null = True)
    nb_employees = models.IntegerField(null = True) 
    def __str__(self):
        return self.name

class Ouvrier (models.Model): 
    client = models.ForeignKey(Client , null = True , on_delete=models.CASCADE)
    job = models.CharField(max_length=50 , null = True)
    desponibility = models.CharField(max_length=50 , null = True)
    description = models.CharField(max_length = 250 , null = True)
    nb_ticket = models.IntegerField(null = True )
    categorie = models.ForeignKey(Categorie , null = True , on_delete= models.CASCADE)
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

class ContactUS (models.Model):
    nom = models.CharField(max_length=50 , null = True)
    email = models.CharField(max_length=250 , null = True)
    message = models.CharField(max_length=500 , null = True) 
    def __str__(self):
        return self.nom
    
class Report (models.Model):
    fromcl = models.ForeignKey(Client ,null = True ,  on_delete = models.CASCADE )
    tocl = models.ForeignKey(Ouvrier , null = True , on_delete= models.CASCADE)
    message = models.CharField(max_length=250 , null = True)
    date_repport = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.fromcl.nom +" send repport for "+ self.tocl.client.nom
    