from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task


@receiver(post_save, sender=Task)
def create_task(sender, instance, created, **kwargs):
    if created:
        print(sender)
        print(instance)
        print(created)
        print('Instance is new')

# @receiver(post_save, sender=Task) 
# def save_task(sender, instance, **kwargs):
# 	instance.title.save()