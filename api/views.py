from django.contrib.auth.models import Group, User
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from todo.settings import EMAIL_HOST_USER

from .models import Task
from .permissions import IsAuthorOrReadOnly
from .serializers import GroupSerializer, TaskSerializer, UserSerializer


def index(request):
    return render(request, 'api/index.html', context={})


class TaskViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given task.

    list:
    Return a list of all the existing tasks.

    create:
    Create a new task.

    update:
    Update existing task.

    partial_update:
    Partial update existing task.

    destroy:
    Delete the given task.
    """
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
            users = User.objects.filter(groups__in=current_user_groups)

            current = self.request.user
            queryset = Task.objects.all().filter(owner__in=users)
            serializer = TaskSerializer(queryset, many=True)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request):
        task = request.data
        current = self.request.user
        new_Task = Task.objects.create(
            owner=current, title=task["title"], dueDate=task["dueDate"])

        # send_mail('About Task', 'Task created', EMAIL_HOST_USER, [current.email], fail_silently=False)

        new_Task.save()

        serializer = TaskSerializer(new_Task)

        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    update:
    Update existing user.

    partial_update:
    Partial update existing user.

    destroy:
    Delete the given user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request):

        if request.user.is_authenticated:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given group.

    list:
    Return a list of all the existing groups.

    create:
    Create a new group instance.

    update:
    Update existing group.

    partial_update:
    Partial update existing group.

    destroy:
    Delete the given group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
