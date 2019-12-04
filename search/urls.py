from django.urls import path, include

from services.views import serviceListView, serviceDetailView
from .views import searchServiceView
from core.views import loginPage, registerPage, homePage, aboutPage, registerServicePage

urlpatterns = [
    path('', searchServiceView.as_view(), name='detail'),

    path('', homePage, name='home'),
    path('index', homePage, name='home'),
    path('index.html', homePage, name='home'),

    path('about', aboutPage, name='about'),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('registerService', registerServicePage, name='registerService'),
]
