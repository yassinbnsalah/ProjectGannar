
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import serializers

from accounts.models import Client, Demmande

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class DemandeSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Demmande
        fields = ('id' , 'job' , 'disponible' , 'description')
        

class ClientSerializer(serializers.ModelSerializer):
    class Meta :
        model = Client
        fields = ('id' , 'nom' , 'prenom' ,'email' ,'is_employees' ,'numero_tel','adress')
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")