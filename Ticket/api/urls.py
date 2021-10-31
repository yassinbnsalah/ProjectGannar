from django.urls import path, include

from Ticket.api.views import ListeTicketAPIView, SendTicketAPIView

urlpatterns = [
    path('send/<int:pk>/' , SendTicketAPIView.as_view()),
    path('liste', ListeTicketAPIView.as_view())
]
