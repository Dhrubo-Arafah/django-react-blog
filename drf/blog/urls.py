from django.urls import path

from .views import BlogListAPIView, BlogCreateAPIView, BlogRetrieveAPIView

urlpatterns = [
    path('api/',BlogListAPIView.as_view()),
    path('create/', BlogCreateAPIView.as_view()),
    path('retrieve/<pk>', BlogRetrieveAPIView.as_view()),
 ]