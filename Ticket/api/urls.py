from django.urls import path, include

from Ticket.api.views import AcceptTicketAPIView, ListeTicketAPIView, RefuseTicketAPIView, SendTicketAPIView

urlpatterns = [
    path('send/<int:pk>/' , SendTicketAPIView.as_view()),
    path('accept/<str:pk>/' , AcceptTicketAPIView.as_view()),
    path('refuser/<str:pk>/' , RefuseTicketAPIView.as_view()),
    path('liste', ListeTicketAPIView.as_view())
]
 