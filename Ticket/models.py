from django.db import models
from accounts.models import Client , Ouvrier
# Create your models here.
class Content_ticket(models.Model):
    date_send = models.DateField(auto_now=True , null = True)
    desciption = models.CharField(max_length = 250 , null = True)
    
class Ticket (models.Model):
    from_client = models.ForeignKey (Client , null = True , on_delete = models.CASCADE)
    to_ouvrier = models.ForeignKey(Ouvrier , null = True , on_delete = models.CASCADE)
    content = models.ForeignKey(Content_ticket , null = True , on_delete=models.CASCADE)
    def __str__(self):
        return "from "+self.from_client.nom+" to "+self.to_ouvrier.client.nom 

