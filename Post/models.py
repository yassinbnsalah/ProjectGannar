from django.db import models

from accounts.models import Categorie, Client

# Create your models here.
class Commentaire(models.Model):
    author = models.ForeignKey(Client , on_delete= models.CASCADE, null = True)
    content = models.CharField(max_length = 500 , null = True)
    date_add = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.author.nom+" just created commentaire "
    
class Post(models.Model):
    client = models.ForeignKey(Client , null = True , on_delete= models.CASCADE)
    content = models.CharField(max_length=500 , null = True) 
    date_post = models.DateField(auto_now_add=True)

    commentaires = models.ManyToManyField(Commentaire)
    def __str__(self):
        return self.client.nom

