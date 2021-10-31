
from django.urls import path, include

from knox.views import LogoutView

from .views import ClientRefuseRoleAPIView, ClientRoleAPIView, DemandeAPIView, ListeClientAPIView, UserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('send', DemandeAPIView.as_view()),
    path('accept_employees/<int:pk>/' , ClientRoleAPIView.as_view()),
    path('refuse_role/<int:pk>/' , ClientRefuseRoleAPIView.as_view()),
    path('list_client/', ListeClientAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout')
]