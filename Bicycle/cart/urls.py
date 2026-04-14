from django.urls import path 

from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name = 'view_cart'),   
    
    path('add/', views.AddToCartView.as_view(), name='add_to_cart'),
    
]