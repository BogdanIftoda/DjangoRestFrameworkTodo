from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField()

    def __str__(self):
        return self.title
