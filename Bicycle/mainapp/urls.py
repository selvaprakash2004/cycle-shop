from django.urls import path
from .views import homeView
from .views import aboutView
from .views import contactView

from . import views

urlpatterns = [
    path('',homeView, name = 'home_page'),
    path('about/',aboutView, name = 'about_page'),
    path('contact/',contactView, name = 'contact_page'),

     path('search', views.searchView, name = 'search_view'),

    path('carousels/', views.CarouselImageList.as_view(), name = 'carousel_list'),
    path('carousels/add/', views.AddCarouselImage.as_view(), name = 'add_carousel'),
    path('carousels/add/<int:pk>/', views.UpdateCarouselImage.as_view(), name = 'edit_carousel'),
    path('carousel/del/<int:pk>', views.DeleteCarouselImage.as_view(), name='del_carousel')
]