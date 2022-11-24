from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User,Profile
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer




class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "user","Location","About","title"
        ]



class CustomSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name','username','email','cretated_at'
        ]

class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=120)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.save
        return user