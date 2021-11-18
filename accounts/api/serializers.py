
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import fields

from rest_framework import serializers

from accounts.models import Categorie, Client, Demmande, Ouvrier, Request_Role

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','groups')

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False)
    class Meta :
        model = Client
        fields = ('id' , 'nom' , 'prenom' ,'email' ,'is_employees' ,'numero_tel','adress' , 'image' ,'user')


class ClientInfoSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Client
        fields = ('id' , 'nom' , 'prenom' ,'email' ,'is_employees' ,'numero_tel','adress','image')

class ClientInfoSerializer2(serializers.ModelSerializer):
    
    class Meta :
        model = Client
        fields = ('id' , 'nom' , 'prenom' ,'email' ,'is_employees' ,'numero_tel','adress')
class DemandeSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    class Meta : 
        model = Demmande
        fields = ('id','job' , 'disponible' , 'description' ,'client')

class CategorieSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Categorie 
        fields = '__all__'
        
class DemandeSendSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Demmande
        fields = ('id','job' , 'disponible' , 'description')
class OuvrierSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many = False)
    class Meta : 
        model = Ouvrier
        fields = ('id' ,'job' ,'desponibility' , 'description','client')

class OuvrierInfoSerializer(serializers.ModelSerializer):
    
    class Meta : 
        model = Ouvrier
        fields = ('id' ,'job' ,'desponibility' , 'description')

class RequestRoleSerializer(serializers.ModelSerializer):
    class Meta :
        model = Request_Role
        fields = ('id' , 'client' , 'demande')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],

        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            
            client = Client.objects.get(user = user)
            print(client.is_employees)
            return client
        raise serializers.ValidationError("Incorrect Credentials")

class LoginAdminSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active and user.groups.filter(name="admin").exists():
            return user
        raise serializers.ValidationError("not admin")

