# from rest_framework import viewsets
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer


def index(request):
    return render(request, 'api/index.html', context={})



class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)