from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from .models import Task
from .serializers import TaskSerializer, UserSerializer, GroupSerializer


def index(request):
    return render(request, 'api/index.html', context={})



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

    
    def create(self,request):
        task = request.data
        current = self.request.user
        new_Task = Task.objects.create(owner=current, title=task["title"])

        new_Task.save()

        serializer = TaskSerializer(new_Task)
        
        return Response(serializer.data)
        


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
