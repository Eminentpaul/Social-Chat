from django.db import models
from base.models import User


# Create your models here.
# class ChatList(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     chat_list = models.ManyToManyField(User, blank=True, related_name='chat_list')
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.owner.first_name
    
#     class Meta:
#         ordering = ['-updated', '-created']
    
    

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    chat_list = models.ManyToManyField(
        User, related_name='chat_lsist', blank=True) 
    image = models.ImageField(null=True, blank=True, upload_to='chats')
    body = models.CharField(null=True, blank=True, max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __unicode__(self):
        return self.body
    

    

    