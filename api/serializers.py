# from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User

from rest_framework import serializers
from .models import Task

# class OwnerField(serializers.Field):
#     user = User()
#     def to_representation(self, value):
#         print(value.username)
#         if 
#         return f"{value.user.id}, {value.username}"
        
#     def to_internal_value(self, data):
        
#         if not isinstance(data, str):
#             msg = 'Incorrect type. Expected a string, but got %s'
#             raise ValidationError(msg % type(data).__name__)
        
#         data = data.split(',')
#         # data = data.split(',')
#         print(data)
#         id_ = int(data[0])
#         username = data[1]
#         return TaskSerializer()




class GroupSerializer(serializers.ModelSerializer):

    class Meta:

        model = Group
        fields = ['name']





class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)    

    class Meta:
        
        model = User
        # model = get_user_model()
        # fields = ('id', 'username', 'groups',)
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    # owner = OwnerField()
    owner = UserSerializer(many=True)

    class Meta:

        model = Task
        # fields = ('id', 'owner', 'title', 'created',)
        fields = '__all__'


