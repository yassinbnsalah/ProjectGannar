from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics, permissions, serializers
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from accounts.decorators import allowed_users
from accounts.models import Categorie, Client, Demmande, Ouvrier
from knox.models import AuthToken
from rest_framework.parsers import JSONParser
#from knox import AuthToken

from .serializers import CategorieSerializer, ClientInfoSerializer, ClientInfoSerializer2, ClientSerializer, DemandeSendSerializer, DemandeSerializer, LoginAdminSerializer, OuvrierInfoSerializer, OuvrierSerializer, RequestRoleSerializer, UserSerializer, RegisterSerializer, LoginSerializer


class UserAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer
    queryset = '' 
    def get(self, request, *args, **kwargs):
        snippets = Client.objects.get(user = self.request.user) 
        print(snippets.nom)
        serializer = ClientSerializer(snippets)
        return JsonResponse(serializer.data, safe=False)

class UpdateClientInfoAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientInfoSerializer2 
    queryset = ''
    def put(self , request ):
        client = Client.objects.get(user = self.request.user)
        data = JSONParser().parse(request)
        serializer = ClientInfoSerializer2(client , data = data)
        if serializer.is_valid():
            serializer.save()
            self.request.user.username = client.nom
            self.request.user.save()
            
            return JsonResponse(serializer.data)
        return Response( ClientInfoSerializer(client).data)

class UpdateClientImageAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientInfoSerializer2 
    queryset = ''
    def put(self , request ):
        print('hello')
        print(request.FILES['images'])
        client = Client.objects.get(user = self.request.user)
        client.image = request.FILES['images']
        client.save()
        return Response( ClientInfoSerializer(client).data)
class UpdateOuvrierInfoAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OuvrierInfoSerializer 
    queryset = ''
    def put(self , request ):
        data = JSONParser().parse(request)
        client = Client.objects.get(user = self.request.user)
        ouvrier = Ouvrier.objects.get(client = client)
        serializer = OuvrierInfoSerializer(ouvrier ,data = data)
        if serializer.is_valid():
            serializer.save()
            print('done')
            return JsonResponse(serializer.data)
        return Response( OuvrierInfoSerializer(ouvrier).data)


class DemandeAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DemandeSendSerializer 
    queryset = ''
    def post(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name='ouvrier').exists():
            return HttpResponse(status=400)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            demande = serializer.save()
            client = Client.objects.get(user = self.request.user)
            demande.client = client
            demande.save() 
            print(self.request.user)
            return Response( UserSerializer(self.request.user).data)


class ClientRoleAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer
    queryset = ''
    def put(self,request, pk):
        try:
            demande = Demmande.objects.get(pk=pk)
        except Demmande.DoesNotExist:
            return HttpResponse(status=404)
        if self.request.user.groups.filter(name='admin').exists():
            print(demande.job)
            client = Client.objects.get(id = demande.client.id)
            group = Group.objects.get(name='ouvrier')
            client.user.groups.add(group)
            client.is_employees = True
            client.save()
            nb = Categorie.objects.filter(name = demande.job).count()
            print(nb)
            if nb == 0:
                categorie = Categorie.objects.get(id = 2)
            else:
                categorie = Categorie.objects.get( name__icontains = demande.job)
            print( categorie.name )
            ouvrier = Ouvrier(client = client , job = demande.job , desponibility = demande.disponible , description = demande.description , categorie = categorie)
            print(ouvrier.categorie.name)
            ouvrier.save()
            demande.delete() 
            return Response(UserSerializer(self.request.user).data)
        else:
            return Response("is not admin")

class ClientRefuseRoleAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer
    queryset = '' 
    def put(self,request,pk):
        try:
            demmande = Demmande.objects.get(pk=pk)
        except Demmande.DoesNotExist:
            return HttpResponse(status=404)
        
        demmande.delete() 
        #Role.delete()
        client = Client.objects.get(user = self.request.user) 
        return Response( ClientSerializer(client).data)

class ListeClientAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer
    queryset = '' 
    def get(self, request, *args, **kwargs):
        snippets = Client.objects.all()
        #snippets = Client.objects.get(user = self.request.user) 
        #print(snippets.nom)
        serializer = ClientSerializer(snippets , many = True)
        return JsonResponse(serializer.data, safe=False)

class ListeOuvrierAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OuvrierSerializer
    queryset = '' 
    def get(self , request , *args, **kwargs):
        liste = Ouvrier.objects.all() 
        serializer = OuvrierSerializer(liste , many=True)
        return JsonResponse(serializer.data , safe = False)

class ListeCategorie(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CategorieSerializer
    queryset = ''
    def get(self , request , *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories , many = True)
        return JsonResponse(serializer.data , safe = False)

class EmployesIDAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OuvrierSerializer 
    queryset = ''
    def get(self , request , pk):
        employes = Ouvrier.objects.get(id = pk)
        serializer = OuvrierSerializer(employes , many = False)
        return JsonResponse(serializer.data , safe = False)
class ListeRequestAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DemandeSerializer
    queryset = '' 
    def get(self , request , *args, **kwargs):
        liste = Demmande.objects.all()
        serializer = DemandeSerializer(liste , many=True)
        return JsonResponse(serializer.data , safe = False)

class RechercherWithNameAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OuvrierSerializer
    queryset = ''
    def get(self , request , name):
        if name == "" :
            employees = Client.objects.filter(is_employees = True)
        else :
        
            employees = Client.objects.filter(nom__icontains = name , is_employees = True)
        liste = list()
        for employ in employees :
            print(employ.nom)
            ouv = Ouvrier.objects.get(client = employ)
            liste.append(ouv)
        serializer = OuvrierSerializer(liste , many = True)
        return JsonResponse(serializer.data , safe = False)

class RecommendedAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OuvrierSerializer
    queryset = ''
    def get(self , request):
        me = Client.objects.get(user = self.request.user)
        print(self.request.user)
        print(me.adress)
        liste = list()
        workers = Client.objects.filter(adress = me.adress , is_employees = True )
        for work in workers:
            if (work.user != self.request.user):
                ouv = Ouvrier.objects.get(client = work)
                liste.append(ouv) 
        serializer = OuvrierSerializer(liste ,many = True)
        return JsonResponse(serializer.data , safe = False)
        

class RechercherPerCatAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = OuvrierInfoSerializer
    queryset = ''
    def get(self , request , job , adress):
        employees = Client.objects.filter(adress = adress)
        
        liste =list()
        for employe in employees:
            ouv = Ouvrier.objects.get(job = job)
            liste.append(ouv)
        print(liste)
        serializer = OuvrierInfoSerializer(liste , many = True)
        return JsonResponse(serializer.data , safe = False)

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        group = Group.objects.get(name='client')
        user.groups.add(group)
        client = Client(nom = user.username , prenom = "" , email = user.email , user = user )
        client.save() 
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.validated_data
        user = client.user
        return Response({
            "user": ClientSerializer(client, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAdminAPIView(generics.GenericAPIView):
    serializer_class = LoginAdminSerializer
    def post(self , request , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
    queryset = ''
    def post(self , request , *args, **kwargs):
        print("")
        logout(self.request.user)
        print("done")
        return Response({
            "done" : "yes"
        })


