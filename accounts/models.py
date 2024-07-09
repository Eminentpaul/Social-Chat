from django.db import models
from base.models import User
from django.templatetags.static import static

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Last Name')
    location = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='profile')
    cover_photo = models.ImageField(null=True, blank=True, upload_to='cover')
    phone_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Phone Number")

    website = models.CharField(max_length=200, blank=True, null=True)
    school_degree = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='School Degree')

    followers = models.ManyToManyField(
        User, related_name='followers', null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def display_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.user.username

    @property
    def avatar(self):
        try:
            if self.image.url:
                avatar = self.image.url
        except:
            avatar = static('assets/images/avatar-1.png')

        return avatar

    @property
    def cover_pic(self):
        try:
            if self.cover_photo.url:
                avatar = self.cover_photo.url
        except:
            avatar = static('assets/images/profile-cover-img.png')

        return avatar


class FriendRequest(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    accepter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='accepter')
    is_accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.sender.first_name

    class Meta:
        verbose_name = 'Friend Request'
        ordering = ['-created']


class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend')
    is_blocked = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.friend.first_name} {self.friend.last_name}"

    def get_full_name(self):
        return f"{self.friend.first_name} {self.friend.last_name}"

    class Meta:
        ordering = ['friend']
