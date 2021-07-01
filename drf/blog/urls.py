from django.urls import path

from .views import BlogListAPIView, BlogCreateAPIView

urlpatterns = [
    path('api/',BlogListAPIView.as_view()),
    path('create/', BlogCreateAPIView.as_view())
]
