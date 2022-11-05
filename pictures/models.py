from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    name =models.CharField(max_length=50)
    user= models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    category=models.CharField(max_length=50,null=True)
    lat=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)
    lng=models.DecimalField(max_digits = 5,decimal_places = 2,null=True)


    def __str__(self):
        
        return self.name


