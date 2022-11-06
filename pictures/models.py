from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name =models.CharField(max_length=50)
#     category=models.CharField(max_length=50,null=True)
#     lat=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
#     lng=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
#     USERNAME_FIELD='name'
#     REQUIRED_FIELDS=[]


class Person(models.Model):
    name =models.CharField(max_length=50)
    user= models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    category=models.CharField(max_length=50,null=True)
    lat=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
    lng=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)


    def __str__(self):
        return self.name


class Message(models.Model):
    post=models.CharField(max_length=200)
    created_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name='x')
    recieved_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE, related_name='y')

    def __str__(self):
        return self.post


