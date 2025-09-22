from django.urls import path
from . import views

from .constants import LIST_CREATE, RETRIEVE_UPDATE_DESTROY
urlpatterns = [
    path('', views.CategoryListCreateAPIView.as_view()),
    path('category/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('product/', views.ProductListCreateAPIView.as_view()),
    path('product/<int:id>/', views.ProductDetailAPIView.as_view()),
    path('', views.film_list_create_api_view),
    path('<int:id>/', views.film_detail_api_view)]