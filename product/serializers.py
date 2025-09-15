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
    
class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    rating = serializers.FloatField(min_value=0, max_value=5)
    stars = serializers.FloatField(request=False)

class CatagoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()
    product_count = serializers.IntegerField()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(min_lengh=1)
    price = serializers.FloatField()
    stars = serializers.FloatField(required=False)