from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.shortcuts import render


from .permissions import IsAuthorOrReadOnly
from .models import Task
from .serializers import TaskSerializer, UserSerializer


def index(request):
    return render(request, 'api/index.html', context={})



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()