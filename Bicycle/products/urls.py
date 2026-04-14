from django.urls import path

from . import views 


urlpatterns = [
    path('', views.ProductList.as_view(), name = 'product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(),name = 'prod_details'),
    path('add/', views.AddProduct.as_view(), name = 'add_product'),
    path('edit/<int:pk>/', views.UpdateProduct.as_view(), name = 'edit_product'),
    path('del/<int:pk>', views.DeleteProduct.as_view(), name='del_product'),

    # product_image
    path('image/<int:pk>/edit/', views.UpdateProductImage.as_view(), name = 'edit_prod_image'),
    path('image/<int:pk>/del/', views.DeleteProductImage.as_view(), name = 'del_prod_image')
]