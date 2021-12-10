
from django.urls import path, include
from knox import views as knox_views

from .views import AcceptReportAPIView, AddCategorieAPIView, ClientRefuseRoleAPIView, ClientRoleAPIView, ContactUSListAPIView, ContactUsAPIView, DeleteCategorieAPIView, DemandeAPIView, EmployesIDAPIView, ListeCategorie, ListeClientAPIView, ListeOuvrierAPIView, ListeReportAPIView, ListeRequestAPIView, LoginAdminAPIView, LogoutAPIView, RechercherPerCatAPIView, RechercherWithNameAPIView, RecommendedAPIView, RefuseReportAPIView, ReportAddAPIView, UpdateClientImageAPIView, UpdateClientInfoAPIView, UpdateOuvrierInfoAPIView, UserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', knox_views.LogoutView.as_view(), name='logout'),
    path('admin/login' , LoginAdminAPIView.as_view()),
    path('send', DemandeAPIView.as_view()),
    path('accept_employees/<int:pk>/' , ClientRoleAPIView.as_view()),
    path('refuse_role/<int:pk>/' , ClientRefuseRoleAPIView.as_view()),
    path('list_client/', ListeClientAPIView.as_view()),
    path('updateInfo/client' , UpdateClientInfoAPIView.as_view()),
    path('updateImage/client' ,  UpdateClientImageAPIView.as_view()),
    path('updateInfo/Ouvrier' , UpdateOuvrierInfoAPIView.as_view()),
    path('list_ouvrier/' , ListeOuvrierAPIView.as_view()),
    path('ouvrier/<str:pk>/' , EmployesIDAPIView.as_view()),
    path('listRequest/' , ListeRequestAPIView.as_view()),
    path('listeCategorie/', ListeCategorie.as_view()),
    path('addCategorie/', AddCategorieAPIView.as_view()),
    path('deleteCategorie/<str:id>/' , DeleteCategorieAPIView.as_view()),
    path('recherchePerName/<str:name>/', RechercherWithNameAPIView.as_view()),
    path('recherchePerCat/<str:job>/<str:adress>' , RechercherPerCatAPIView.as_view()),
    path('sugUser/' , RecommendedAPIView.as_view()),
    path('contactUS/' , ContactUsAPIView.as_view()),
    path('contactUS/liste', ContactUSListAPIView.as_view()),
    path('report/add/<str:id>/' , ReportAddAPIView.as_view()),
    path('report/liste/' , ListeReportAPIView.as_view()),
    path('report/accepte/<str:id>/' , AcceptReportAPIView.as_view()), 
    path('report/delete/<str:id>/' , RefuseReportAPIView.as_view())
  
]