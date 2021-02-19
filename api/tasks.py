import random
import string

from celery import shared_task

from django.contrib.auth.models import Group 


@shared_task

def create_new_object():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])

    new_object = Group.objects.create(name=random_name)
    return new_object