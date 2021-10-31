from django.contrib.auth.models import Group
from django.http.response import HttpResponse, JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from accounts.models import Client, Demmande, Ouvrier, Request_Role
from knox.models import AuthToken
#from knox import AuthToken

from .serializers import ClientSerializer, DemandeSerializer, UserSerializer, RegisterSerializer, LoginSerializer


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
    def get_object(self):
        print(self.request.user)
        return self.request.user

class DemandeAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = DemandeSerializer 
    queryset = ''
    #queryset = Demmande.objects.all()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        demande = serializer.save()
        demande.save()
        client = Client.objects.get(user = self.request.user)
        request_role = Request_Role(client = client , demande = demande)
        request_role.save() 
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
            Role = Request_Role.objects.get(pk=pk)
        except Request_Role.DoesNotExist:
            return HttpResponse(status=404)
        
        client = Client.objects.get(id = Role.client.id)
        group = Group.objects.get(name='ouvrier')
        client.user.groups.add(group)
        client.is_employees = True
        client.save()
        demmande = Demmande.objects.get(id = Role.demande.id)
        ouvrier = Ouvrier(client = client , job = demmande.job , desponibility = demmande.disponible , description = demmande.description)
        ouvrier.save()
        demmande.delete() 
        Role.delete()
        return Response( UserSerializer(self.request.user).data)

class ClientRefuseRoleAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer
    queryset = '' 
    def put(self,request,pk):
        try:
            Role = Request_Role.objects.get(pk=pk)
        except Request_Role.DoesNotExist:
            return HttpResponse(status=404)
        demmande = Demmande.objects.get(id = Role.demande.id)
        demmande.delete() 
        Role.delete()
        return Response( UserSerializer(self.request.user).data)

class ListeClientAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ClientSerializer
    queryset = '' 
    def get(self, request, *args, **kwargs):
        snippets = Client.objects.all()
        serializer = ClientSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        group = Group.objects.get(name='client')
        user.groups.add(group)
        client = Client(nom = user.username , prenom = "" , email = user.email , user = user)
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
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

