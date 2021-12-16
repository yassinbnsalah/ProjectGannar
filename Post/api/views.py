
from django.http.response import HttpResponse, JsonResponse
from typing import Generic
from django.shortcuts import redirect
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from Post.models import Commentaire, Post
from accounts.api.serializers import ClientSerializer, UserSerializer
from accounts.models import Client, Ouvrier
from .serializers import CommentaireInfoSerializer, CommentaireSerializer, PostSerializer,PostListeSerializer

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
    serializer_class = CommentaireInfoSerializer
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

class CommentaireAddAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CommentaireSerializer
    queryset = ''
    def post(self , request , id):
        post = Post.objects.get(id = id)
        print(post.content)
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        commentaire = serializer.save()
        client = Client.objects.get(user = self.request.user)
        commentaire.author  = client 
        
        commentaire.save()
        post.commentaires.add(commentaire)
        post.save()
        serializer = ClientSerializer(client , many = False) 
        return JsonResponse(serializer.data , safe = False) 

class ListeCommentaireAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CommentaireInfoSerializer
    queryset = ''
    def get(self , request):
        
        liste_commentaire = Commentaire.objects.all() 
        
        serializer = CommentaireInfoSerializer(liste_commentaire , many = True)
        return JsonResponse(serializer.data , safe = False)

class DeletePostAPIView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = ''
    def delete(self , request ,id):
        post = Post.objects.get(id = id)
        post.delete()
        return JsonResponse("done",  safe = False)