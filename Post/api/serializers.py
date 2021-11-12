

from Post.models import Post

from rest_framework import serializers

from accounts.api.serializers import ClientSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id','content')


class PostListeSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    class Meta :
        model = Post 
        fields = ('id', 'content' , 'client' , 'date_post')
