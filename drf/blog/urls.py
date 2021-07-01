from django.urls import path

from .views import BlogListAPIView

urlpatterns = [
    path('api/',BlogListAPIView.as_view())
]
