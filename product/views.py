from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer

# Create your views here.
@api_view(http_method_names=['GET'])
def categories_list_api_view(request):
    categories = Category.objects.annotate(products_count=Count('products'))
    data = CategorySerializer(categories, read_only = True)
    list_categories = []
    for i in product:
        list.append(model_to_dict(i, fields=['id', 'text', 'title', 'price']))
    
    return Response(data=list_categories)

def products_list_api_view(request):
    products = Product.objects.select_related('reviews').all()
    data = ProductSerializers(products, many = True)
    list_products = []
    return Response(data= list_products)
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    list_reviews = []
    return Response(data=list_reviews)