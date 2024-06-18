from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, unique=False)
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last Name')
    email = models.EmailField(unique=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile')
    location = models.CharField(max_length=200, blank=True, null=True)
    is_online = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.first_name
    
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    