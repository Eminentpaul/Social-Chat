from django.contrib import admin
from .models import FriendRequest, Contact, Profile

# Register your models here.
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['sender', 'accepter', 'is_accepted', 'created']
    
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend', 'is_blocked', 'created']
    

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location']

admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Contact, ContactAdmin)     
admin.site.register(Profile, ProfileAdmin)