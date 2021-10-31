from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import serializers

from Ticket.models import Content_ticket, Ticket

class TicketContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content_ticket
        fields = ('id' , 'desciption')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'