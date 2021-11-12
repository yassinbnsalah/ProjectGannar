
from django.urls import path, include

from knox.views import LogoutView

from .views import ClientRefuseRoleAPIView, ClientRoleAPIView, DemandeAPIView, ListeClientAPIView, ListeOuvrierAPIView, ListeRequestAPIView, LoginAdminAPIView, LogoutAPIView, RechercherPerCatAPIView, RechercherWithNameAPIView, RecommendedAPIView, UpdateClientInfoAPIView, UserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('admin/login' , LoginAdminAPIView.as_view()),
    path('send', DemandeAPIView.as_view()),
    path('accept_employees/<int:pk>/' , ClientRoleAPIView.as_view()),
    path('refuse_role/<int:pk>/' , ClientRefuseRoleAPIView.as_view()),
    path('list_client/', ListeClientAPIView.as_view()),
    path('updateInfo/client' , UpdateClientInfoAPIView.as_view()),
    path('list_ouvrier/' , ListeOuvrierAPIView.as_view()),
    path('listRequest/' , ListeRequestAPIView.as_view()),
    path('recherchePerName/<str:name>/', RechercherWithNameAPIView.as_view()),
    path('recherchePerCat/<str:job>/<str:adress>' , RechercherPerCatAPIView.as_view()),
    path('recommended/' , RecommendedAPIView.as_view()),
    path('logout', LogoutAPIView.as_view())
]