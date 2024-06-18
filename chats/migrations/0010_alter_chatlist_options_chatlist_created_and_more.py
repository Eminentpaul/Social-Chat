# Generated by Django 5.0.6 on 2024-06-15 14:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0009_chatlist_message_chat_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatlist',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='chatlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatlist',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
