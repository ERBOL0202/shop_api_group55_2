from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer

# Create your views here.
@api_view(http_method_names=['GET', 'POST', 'PUT', 'DELETE'])
def categories_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(products_count=Count('products'))
        data = CategorySerializer(categories, read_only = True)
        list_categories = []
        for i in product:
            list.append(model_to_dict(i, fields=['id', 'text', 'title', 'price']))
    
        return Response(data=list_categories)
    elif request.method == 'POST':
        return Response()
    elif request.method == 'PUT':
        categories.name = request.data.get('name')
        return Response(status=status.HTTP_201_CREATED,
                        data=CategorySerializer(categories).data)

@api_view(http_method_names=['GET', 'POST', 'PUT', 'DELETE'])
def products_list_create_api_view(request):
    products = Product.objects.select_related('reviews').all()
    if request.method == 'GET':
        data = ProductSerializers(products, many = True)
        list_products = []
        return Response(data= list_products)
    elif request.method == 'PUT':
        products.title = request.data.get('title')
        products.description = request.data.get('description')
        products.price = request.data.get('price')
        products.rating = request.data.get('rating')
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductSerializer(products).data)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['POST', 'PUT', 'DELETE'])
def reviews_list_create_api_view(request):
    reviews = Review.objects.all()
    list_reviews = []
    return Response(data=list_reviews)
    if request.method == 'POST':
        reviews.text = request.data.get('text')
        reviews.product = request.data.get('product')
        reviews.stars = request.data.get('stars')

    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.product = request.data.get('product')
        reviews.stars = request.data.get('stars')
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
