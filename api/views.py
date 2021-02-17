# from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import permissions


from .permissions import IsAuthorOrReadOnly, IsGroupOrReadOnly
from .models import Task
from .serializers import TaskSerializer, UserSerializer, GroupSerializer


def index(request):
    return render(request, 'api/index.html', context={})



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthorOrReadOnly, IsGroupOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (IsGroupOrReadOnly,)
