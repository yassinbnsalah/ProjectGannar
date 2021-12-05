

from django.db.models import fields
from Post.models import Commentaire, Post

from rest_framework import serializers

from accounts.api.serializers import ClientSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id','content')
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Commentaire
        fields = ('id', 'content')

class PostListeSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    
    class Meta :
        model = Post
        fields = ('id', 'content' , 'client' , 'date_post' )
class CommentaireInfoSerializer(serializers.ModelSerializer):
    Post_related = PostSerializer(many = False)
    class Meta : 
        model = Commentaire
        fields = ('id', 'content', 'author' ,'date_add' ,'Post_related')

