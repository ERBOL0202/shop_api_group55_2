from rest_framework import serializers
from .models import Product, Review, Category


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text rating'.split()

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField()
    class Meta:
        model = Category
        fields = 'id title product_count'.split()

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only = True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = 'id title discription avarage_rating review'.split()
    
    def get_avarage_rating(self, product):
        reviews = product.reviews.all
        if reviews:
            return round(sum(i.rating for i in reviews) / reviews.count())
        return None
    
