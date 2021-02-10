from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer
from .models import Task


@receiver(post_save, sender=Task)
def notify_task_save(sender, **kwargs):
    if "instance" in kwargs:
        instance = kwargs["instance"]
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "task", {"type": "user_notification",
                     "event": "New Notification",
                     "notification": instance.title,
                     "id": instance.id}
        )

@receiver(post_delete, sender=Task)
def notify_task_delete(sender, instance, **kwargs):
    Task.objects.filter(id=instance.id).delete()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "task", {"type": "delete_task",
                "event": "Delete Task",
                "notification": instance.title,
                "id": instance.id
        }
    )
    
