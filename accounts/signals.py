from django.dispatch import receiver
from django.db.models.signals import post_save
from base.models import User
from .models import Profile

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance
    
    # Adding Profile for a new registered user
    if created:
        Profile.objects.create(user=user)