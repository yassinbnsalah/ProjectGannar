
from django.http.response import HttpResponse, JsonResponse
from typing import Generic
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from Post.models import Post
from accounts.api.serializers import ClientSerializer, UserSerializer
from accounts.models import Client, Ouvrier
from .serializers import PostSerializer,PostListeSerializer

class AddPostAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]  
    serializer_class = PostSerializer 
    queryset = ''
    def post (self , request ):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        post = serializer.save() 
        client = Client.objects.get( user = self.request.user)
        post.client = client 
        post.save()  
        return Response(UserSerializer(self.request.user).data)


class ListePostAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostListeSerializer
    queryset = '' 
    def get(self , request) :
        client = Client.objects.get(user = self.request.user)
        post = Post.objects.filter(client = client)
        serializer = PostListeSerializer(post , many = True)
        return JsonResponse(serializer.data , safe=False)

class ListePostForEmployeesAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = PostListeSerializer
    queryset = ''
    def get(self , request) :
        client = Client.objects.get(user = self.request.user)
        employees = Ouvrier.objects.get(client = client) 
        client_adress = Client.objects.filter(adress = client.adress) 
        liste = list() 
        for cl in client_adress:
            posts = Post.objects.filter(client = cl) 
            for post in posts:
                liste.append(post)

        print(liste)
        serializer = PostListeSerializer(liste , many = True) 
        return JsonResponse(serializer.data , safe = False)

