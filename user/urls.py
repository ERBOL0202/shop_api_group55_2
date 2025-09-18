from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration_api_view),
    path('authorization/', views.authorization_api_view),
    path('/api/v1/users/confirm/', views.confirmation_api_view)]