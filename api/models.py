from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
