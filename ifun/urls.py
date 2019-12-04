"""ifun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include

from services.views import serviceListView, serviceDetailView

from core import urls
from ifun import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('search/', include("search.urls"), name='search'),

    path('services', serviceListView.as_view(), name='services'),
    path('services/<int:pk>', serviceDetailView.as_view(), name='service'),

    # path('products_fbv', views.aboutPage, name='about'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
