from rest_framework import viewsets

from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


def index(request):
    return render(request, 'api/index.html', context={})