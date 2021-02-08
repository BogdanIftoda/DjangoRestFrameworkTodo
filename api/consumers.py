import json
from channels.generic.websocket import WebsocketConsumer   
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task



class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()   

    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
    # @receiver(post_save, sender=Task) 
    # def create_task(sender, instance, created, **kwargs):
    #     if created:
    #         Task.objects.create(title=instance)

    # @receiver(post_save, sender=Task) 
    # def save_task(sender, instance, **kwargs):
    #     instance.task.save()

