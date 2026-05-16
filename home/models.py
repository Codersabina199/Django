from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.TextField()
    photo=models.ImageField(null=True,upload_to="static/products/")




    def __str__(self):
        return self.name
    




class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name=models.CharField (max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=10)   

    def __str__(self):
        return self.name        


