# Generated by Django 3.2.16 on 2022-11-05 20:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pictures', '0010_auto_20221105_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created_by',
        ),
        migrations.AddField(
            model_name='message',
            name='created_by',
            field=models.ManyToManyField(null=True, related_name='x', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='message',
            name='recieved_by',
        ),
        migrations.AddField(
            model_name='message',
            name='recieved_by',
            field=models.ManyToManyField(null=True, related_name='y', to=settings.AUTH_USER_MODEL),
        ),
    ]
