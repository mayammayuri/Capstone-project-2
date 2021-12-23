from django.urls import path
from . import views

urlpatterns = [
    path('apple/', views.apple_stock_api),
    path('adidas/', views.adidas_stock_api),
    path('zara/', views.zara_stock_api),
    path('fb/', views.facebook_stock_api),
    path('tatam/', views.tata_stock_api),
    path('accenture/', views.accenture_stock_api),
    path('adobe/', views.adobe_stock_api),
    path('amazon/', views.amazon_stock_api),
    path('cisco/', views.cisco_stock_api),
    path('colgate/', views.colgate_stock_api),
    path('fortis/', views.fortis_stock_api),
    path('heromotoco/', views.heromotoco_stock_api),
    path('ibm/', views.ibm_stock_api),
    path('johnson/', views.johnson_stock_api),
    path('JPMorgan/', views.JPMorgan_stock_api),
    path('maruti/', views.maruti_stock_api),
    path('netflix/', views.netflix_stock_api),
    path('NVIDIA/', views.NVIDIA_stock_api),
    path('tvsmotors/', views.tvsmotors_stock_api),
    path('pepsi/', views.pepsi_stock_api),
    path('wallmart/', views.wallmart_stock_api),

]
