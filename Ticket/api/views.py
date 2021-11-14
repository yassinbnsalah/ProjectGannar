

from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from rest_framework import generics, permissions, response
from rest_framework.response import Response
from Ticket.api.serializers import TicketContentSerializer, TicketSerializer
from Ticket.models import Ticket
from accounts.api.serializers import UserSerializer
from accounts.models import Client, Ouvrier


class SendTicketAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = TicketContentSerializer
    queryset = '' 
    def post(self, request, pk):
        to_employees = Ouvrier.objects.get( id = pk)
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


