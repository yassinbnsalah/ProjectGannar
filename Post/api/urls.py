
from django.urls import path, include
from Post.api.views import AddPostAPIView, ListePostAPIView

urlpatterns = [
    path('add/' , AddPostAPIView.as_view()),
    path('liste/' ,ListePostAPIView.as_view())
    ]