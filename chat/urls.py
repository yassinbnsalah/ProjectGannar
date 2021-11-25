from django.urls import path

from chat.views import MessageAPIView

urlpatterns = [
    path('messages' , MessageAPIView.as_view()),
]
