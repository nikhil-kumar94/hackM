# Generated by Django 3.2.16 on 2022-11-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0007_auto_20221105_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created',
        ),
        migrations.RemoveField(
            model_name='message',
            name='updated',
        ),
        migrations.AlterField(
            model_name='message',
            name='recieved_by',
            field=models.CharField(max_length=200, null=True),
        ),
    ]