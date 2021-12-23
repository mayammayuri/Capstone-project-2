from django.urls import path
from . import views

urlpatterns = [
    path('apple/', views.apple_stock_api),
    path('adidas/', views.adidas_stock_api),
    path('zara/', views.zara_stock_api),
    path('fb/', views.facebook_stock_api),
    path('tatam/', views.tata_stock_api),
]
