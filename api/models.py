from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField()
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title
