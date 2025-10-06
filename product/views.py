from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer, ReviewValidateSerializer, CatagoryValidateSerializer, ProductValidateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
# Create your views here.

@api_view(http_method_names=['GET', 'POST', 'PUT', 'DELETE'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.select_related('title').prefetch_related('reviews', 'product').all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all
    serializer_class = CategorySerializer

def categories_list_create_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(products_count=Count('products'))
        data = CategorySerializer(categories, read_only = True)
        list_categories = []
        for i in product:
            list.append(model_to_dict(i, fields=['id', 'text', 'title', 'price']))
    
        return Response(data=list_categories)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        name = serializer.validated_data.get('name')
        product_count = serializer.validated_data.get('product_count')
    elif request.method == 'PUT':
        categories.name = request.data.get('name')
        return Response(status=status.HTTP_201_CREATED,
                        data=CategorySerializer(categories).data)

@api_view(http_method_names=['GET', 'POST', 'PUT', 'DELETE'])
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    permission_classes = [(IsOwner, IsAnonymous) | CanEditWithIn15minutes]

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
    permission_classes = [IsModerator]

def products_list_create_api_view(request):
    products = Product.objects.select_related('reviews').all()
    if request.method == 'GET':
        data = ProductSerializers(products, many = True)
        list_products = []
        return Response(data= list_products)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        products.title = serializer.validated_data.get('title')
        products.description = serializer.validated_data.get('description')
        products.price = serializer.validated_data.get('price')
        products.rating = serializer.validated_data.get('rating')
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
class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all
    serializer_class = ReviewSerializer
    
def reviews_list_create_api_view(request):
    reviews = Review.objects.all()
    list_reviews = []
    return Response(data=list_reviews)
    if request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        reviews.text = serializer.validated_data.get('text')
        reviews.product = serializer.validated_data.get('product')
        reviews.stars = serializer.validated_data.get('stars')

    elif request.method == 'PUT':
        reviews.text = request.data.get('text')
        reviews.product = request.data.get('product')
        reviews.stars = request.data.get('stars')
        return Response(status=status.HTTP_201_CREATED,
                        data=ReviewSerializer(reviews).data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
