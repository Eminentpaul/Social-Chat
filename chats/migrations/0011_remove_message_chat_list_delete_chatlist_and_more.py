# Generated by Django 5.0.6 on 2024-06-16 22:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_alter_chatlist_options_chatlist_created_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat_list',
        ),
        migrations.DeleteModel(
            name='ChatList',
        ),
        migrations.AddField(
            model_name='message',
            name='chat_list',
            field=models.ManyToManyField(blank=True, related_name='chat_lsist', to=settings.AUTH_USER_MODEL),
        ),
    ]
