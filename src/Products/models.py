from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    product = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='This is a cool product')