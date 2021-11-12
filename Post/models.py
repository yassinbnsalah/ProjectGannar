from django.db import models

from accounts.models import Client

# Create your models here.
class Post(models.Model):
    client = models.ForeignKey(Client , null = True , on_delete= models.CASCADE)
    content = models.CharField(max_length=500 , null = True) 
    date_post = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.client.nom