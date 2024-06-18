from django.contrib import admin
from .models import User

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_online' ]
    list_display_links = ['first_name', 'last_name', 'username']

admin.site.register(User, AdminUser)