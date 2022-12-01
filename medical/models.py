from email.policy import default
from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    description=models.CharField(max_length=200)
    image=models.CharField(max_length=2000)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    desc=models.TextField()

    def __str__(self):
        return self.email
class Order(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    items=models.CharField(max_length=1500)
    address=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    phoneno=models.CharField(max_length=10)
    delivery=models.BooleanField (default=False)
    def __int__(self):
        return self.id
class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    feedback=models.TextField()
    
   
        
    