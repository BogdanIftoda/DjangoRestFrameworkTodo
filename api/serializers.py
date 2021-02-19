from django.contrib.auth.models import Group, User

from rest_framework import serializers
from .models import Task

class OwnerField(serializers.ChoiceField):
    
    
    def to_representation(self, value):
        return {
            'id': value.id,
            'username': value.username,
        }
        
    def to_internal_value(self, username):

        user = User.objects.filter(username=username).first()
        # print(user)
        return user


class GroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = Group
        fields = ('name',)



class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, required=False)    

    class Meta:
        
        model = User
        fields = ('id', 'username', 'groups',)



class TaskSerializer(serializers.ModelSerializer):

    owner = OwnerField(choices=User.objects.all(), read_only=True)
    
    class Meta:

        model = Task
        fields = ('id', 'title', 'created', 'owner',)

    