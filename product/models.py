from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)

    
    
class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(max_length=256, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    
class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    
