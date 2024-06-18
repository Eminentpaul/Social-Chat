from django.contrib import admin
from .models import FriendRequest, Contact

# Register your models here.
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['sender', 'accepter', 'is_accepted', 'created']
    
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend', 'is_blocked', 'created']

admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Contact, ContactAdmin)     