from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('index', views.homePage, name='home'),
    path('index.html', views.homePage, name='home'),

    path("base", views.basePage),

    path('about', views.aboutPage, name='about'),
    path('contact', views.contactPage, name='contact'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('registerService', views.registerServicePage, name='registerService'),

]
