from django.urls import path

from .views import BlogListAPIView, BlogCreateAPIView, BlogRetrieveAPIView, BlogUpdateAPIView, BlogDestroyAPIView

urlpatterns = [
    path('api/', BlogListAPIView.as_view()),
    path('create/', BlogCreateAPIView.as_view()),
    path('retrieve/<pk>', BlogRetrieveAPIView.as_view()),
    path('update/<pk>', BlogUpdateAPIView.as_view()),
    path('destroy/<pk>', BlogDestroyAPIView.as_view()),
]
