
from django.urls import path, include
from Post.api.views import AddPostAPIView, ListePostAPIView, ListePostForEmployeesAPIView

urlpatterns = [
    path('add/' , AddPostAPIView.as_view()),
    path('liste/' ,ListePostAPIView.as_view()),
    path('recommended/liste' , ListePostForEmployeesAPIView.as_view())
    ]