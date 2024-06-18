from django.contrib import admin
from .models import Message #ChatList

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'body', 'is_read', 'created']
    
    
# class ChatListAdmin(admin.ModelAdmin):
#     list_display = ['owner', 'chat_list']

admin.site.register(Message, MessageAdmin)
# admin.site.register(ChatList)