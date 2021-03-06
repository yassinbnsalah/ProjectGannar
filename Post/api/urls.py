
from django.urls import path, include
from Post.api.views import AddPostAPIView, CommentaireAddAPIView, DeletePostAPIView, ListeCommentaireAPIView, ListePostAPIView, ListePostForEmployeesAPIView

urlpatterns = [
    path('add/' , AddPostAPIView.as_view()),
    path('delete/<str:id>/' , DeletePostAPIView.as_view()),
    path('liste/' ,ListePostAPIView.as_view()),
    path('recommended/liste' , ListePostForEmployeesAPIView.as_view()),
    path('commentaire/add/<str:id>/' , CommentaireAddAPIView.as_view()),
    
    ]