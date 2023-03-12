from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User , Profile


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        data["email"] = self.user.email
        data["username"] = self.user.username

        
        make_password(self.user.password)

        return data

    


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username" , "password"]

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username = validated_data["username"],                
            password=make_password(validated_data["password"]),
        )
        
        user.save()
        return user
    

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

