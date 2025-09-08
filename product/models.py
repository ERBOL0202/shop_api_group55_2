from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)



    
    
class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(max_length=256, null=True)
    rating = models.FloatField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

def __str__(self):
        return self.title

    
STARS = ((i, '*' * i) for i in range(1, 5))

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    stars = models.IntegerField(choices=STARS, default=5)

    def __str__(self):
        return self.text



    
