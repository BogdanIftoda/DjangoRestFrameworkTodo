
from datetime import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from todo.settings import EMAIL_HOST_USER

from .models import Task


@shared_task
def sending_email_task():
    
    tasks = Task.objects.all()
    current_date = (datetime.now().timestamp()/60)

    for task in tasks:
        taskDate = (task.dueDate.timestamp())/60

        if ((taskDate - current_date)) <= 120 and ((taskDate - current_date)) > 0:
            
            subject = 'Task {}'.format(task.title)
            message = 'Task is not completed yet, {}'.format(task.dueDate)
            if task.notified == False:
                print(task)
                if (send_mail(subject, message, EMAIL_HOST_USER, [task.owner.email], fail_silently=False)):
                    tasks.update(notified=True)
                    
