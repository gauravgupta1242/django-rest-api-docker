from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from .models import Arule , Customeremotion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AruleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Arule
        fields = ['rules','support','lift', 'target']     




class CustomeremotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customeremotion
        fields = ['index','emotion','count', 'per']

        




