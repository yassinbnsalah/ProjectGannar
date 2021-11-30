

from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from rest_framework import generics, permissions, response, serializers
from rest_framework.response import Response
from Ticket.api.serializers import TicketContentSerializer, TicketSerializer
from Ticket.models import Content_ticket, Ticket
from accounts.api.serializers import ClientSerializer, UserSerializer
from accounts.models import Client, Ouvrier


class SendTicketAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TicketContentSerializer
    queryset = '' 
    def post(self, request, pk):
        to_employees = Ouvrier.objects.get( id = pk)
        to_employees.nb_ticket = to_employees.nb_ticket + 1 
        to_employees.save()
        client = Client.objects.get(user = self.request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticketContent = serializer.save() 
        ticketContent.save()
        ticket = Ticket(from_client = client , to_ouvrier = to_employees , content = ticketContent)
        ticket.save()
        print("done")
        return Response(UserSerializer(self.request.user).data)

class ListeTicketAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TicketSerializer
    queryset = '' 
    def get(self, request , *args, **kwargs):
        client = Client.objects.get(user = self.request.user)
        ouvrier = Ouvrier.objects.get(client = client)
        ticket = Ticket.objects.filter(to_ouvrier = ouvrier)
        serializer = TicketSerializer(ticket, many=True)
        return JsonResponse(serializer.data, safe=False)

class AcceptTicketAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TicketSerializer
    queryset = '' 
    def put (self , request , pk):
        ticket = Ticket.objects.get ( id = pk) 
        ticket.accepted = True 
        ticket.save()
        serializer = TicketSerializer(ticket , many = False)
        return JsonResponse(serializer.data , safe = False)

class RefuseTicketAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TicketSerializer
    queryset = '' 
    def put ( self , request , pk):
        ticket = Ticket.objects.get(id = pk)
        ticket.content.delete()
        ticket.delete() 
        client = Client.objects.get(user = self.request.user)
        serializer = ClientSerializer(client , many = False )
        return JsonResponse(serializer.data , safe = False)