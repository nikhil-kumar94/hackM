# Generated by Django 3.2.16 on 2022-11-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='pic',
        ),
        migrations.AddField(
            model_name='person',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='lat',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='lng',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
