from django.shortcuts import render, redirect
from .models import CarouselImage

# Views.py handles request-response
# It also handles the DML and DQL operations required for the same.

# Create your views here.
from products.models import Product

def homeView(request):
    template = 'mainapp/home.html'
    context = {
        # This will be an array of all active carousel image objects mapped from DB
        'carousel_images' : CarouselImage.objects.filter(is_active = True),
        'products' : Product.objects.all(),
     
        }
    return render(
        request = request,
        template_name= template,
        context= context
    )

def aboutView(request):
    template = 'mainapp/about.html'
    return render(
        request = request,
        template_name= template,
        context={}
    )

def contactView(request):
    template = 'mainapp/contact.html'

    return render(
        request = request,
        template_name= template,
        context={}
    )


# Class based generic views
from django.views.generic import (
    CreateView,
    ListView, DetailView,
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy

class CarouselImageList(ListView):
    template_name = 'mainapp/carousel/carousel_list.html'
    model = CarouselImage
    context_object_name = 'carousel_images'    

class AddCarouselImage(CreateView):
    model = CarouselImage
    template_name = 'mainapp/carousel/add_carousel.html'
    fields = '__all__'
    success_url = reverse_lazy('carousel_list')
    
class UpdateCarouselImage(UpdateView):
    model = CarouselImage
    template_name = 'mainapp/carousel/edit_carousel.html'
    fields = '__all__'
    success_url = reverse_lazy('carousel_list')
    
class DeleteCarouselImage(DeleteView):
    model = CarouselImage
    template_name = 'mainapp/carousel/del_carousel.html'
    success_url = reverse_lazy('carousel_list')
    context_object_name = 'carousel_image' 

# Search Results

from products.models import Product

def searchView(request):
    query = request.GET.get('q')

    if not query:
        return redirect(reverse_lazy('home_page'))
    
    products = Product.objects.filter(title__icontains = query)

    context = {
        'query' : query,
        'products' : products
    }
    template = 'mainapp/search_results.html'
    return render(request, template, context)