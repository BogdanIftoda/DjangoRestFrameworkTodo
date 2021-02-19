from django.contrib.auth.models import Group, User
from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .permissions import IsAuthorOrReadOnly
from .serializers import GroupSerializer, TaskSerializer, UserSerializer


def index(request):
    return render(request, 'api/index.html', context={})


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)

    def list(self, request):

        if request.user.is_authenticated and request.user.is_staff:
            queryset = Task.objects.all()
            serializer = TaskSerializer(queryset, many=True)
            return Response(serializer.data)

        if request.user.is_authenticated:
            current_user_groups = request.user.groups.all()
            print(request.user.groups.all())
            users = User.objects.filter(groups__in=current_user_groups)

            current = self.request.user
            queryset = Task.objects.all().filter(owner__in=users)
            serializer = TaskSerializer(queryset, many=True)
            # queryset1 = User.objects.all().filter(groups=current.groups)
            # serializer_2 = UserSerializer(queryset1)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        task = request.data
        current = self.request.user
        new_Task = Task.objects.create(owner=current, title=task["title"], dueDate=task["dueDate"])

        new_Task.save()

        serializer = TaskSerializer(new_Task)

        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request):

        if request.user.is_authenticated:
            queryset = User.objects.all()
            print(request.user)
            # print(User.objects.filter(groups))
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
