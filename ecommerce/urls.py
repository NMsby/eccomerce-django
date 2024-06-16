from django.urls import path
from . import views

# app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home' ),
    #     path('', views.product_list, name='product_list'),
]

