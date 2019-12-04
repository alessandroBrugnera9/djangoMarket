from django.urls import path, include

from .views import (
    serviceDetailView
)

urlpatterns = [
    path('services/<int:pk>', serviceDetailView.as_view(), name='service'),
]
