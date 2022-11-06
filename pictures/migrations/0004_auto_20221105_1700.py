# Generated by Django 3.2.16 on 2022-11-05 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pictures', '0003_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createdpictures_message_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updatedpictures_message_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
