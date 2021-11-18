from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import serializers

from Ticket.models import Content_ticket, Ticket
from accounts.api.serializers import ClientSerializer, OuvrierInfoSerializer, OuvrierSerializer

class TicketContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content_ticket
        fields = ('id' , 'desciption')

class TicketSerializer(serializers.ModelSerializer):
    from_client = ClientSerializer(many = False)
    to_ouvrier = OuvrierSerializer(many = False) 
    class Meta:
        model = Ticket
        fields = ('id' ,'from_client' ,'to_ouvrier' , 'content' ,'accepted')