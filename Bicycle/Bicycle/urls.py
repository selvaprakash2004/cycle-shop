"""
URL configuration for Bicycle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# adding these imports to support media hosting in development server
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('products/', include('products.urls')),

    path('accounts/', include('authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('cart/', include('cart.urls')),

    path('', include('orders.urls')),
    path('',include('payments.urls'))

]

# When the DEBUG variable is set to True in settings.py, we know that the 
# project is still in development.
# During this time, we are seeking help from django to host the media files.
# When we move to production, this stops working for security reasons.
# We'll then reconfigure the project to use an external media server.

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root = settings.MEDIA_ROOT)