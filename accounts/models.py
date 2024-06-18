from django.db import models
from base.models import User

# Create your models here.
class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    accepter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accepter')
    is_accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __unicode__(self):
        return self.sender.first_name
    
    
    class Meta:
        verbose_name = 'Friend Request'
        ordering = ['-created']
        
        
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    is_blocked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.friend.first_name} {self.friend.last_name}"
    
    def get_full_name(self):
        return f"{self.friend.first_name} {self.friend.last_name}"
    
    class Meta:
        ordering = ['friend'] 
    
    