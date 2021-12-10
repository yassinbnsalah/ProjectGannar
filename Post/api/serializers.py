

from django.db.models import fields
from Post.models import Commentaire, Post

from rest_framework import serializers

from accounts.api.serializers import ClientInfoSerializer, ClientSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id','content')
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Commentaire
        fields = ('id', 'content')
class CommentaireInfoSerializer(serializers.ModelSerializer):
    author = ClientInfoSerializer(many = False)
    class Meta : 
        model = Commentaire
        fields = ('id', 'content', 'author' ,'date_add')

class PostListeSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    commentaires = CommentaireInfoSerializer(many = True)
    class Meta :
        model = Post
        fields = ('id', 'content' , 'client' , 'date_post' ,'commentaires')

