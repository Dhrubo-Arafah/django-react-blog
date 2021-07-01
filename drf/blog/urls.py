from django.urls import path

# from .views import BlogListAPIView, BlogCreateAPIView, BlogRetrieveAPIView, BlogUpdateAPIView, BlogDestroyAPIView,
# from .views import BlogListCreateView, BlogDetailView, BlogModelViewSet

#
# urlpatterns = [
#     path('api/', BlogListAPIView.as_view()),
#     path('create/', BlogCreateAPIView.as_view()),
#     path('retrieve/<pk>', BlogRetrieveAPIView.as_view()),
#     path('update/<pk>', BlogUpdateAPIView.as_view()),
#     path('destroy/<pk>', BlogDestroyAPIView.as_view()),
#     path('api/', BlogListCreateView.as_view()),
#     path('detail/<pk>', BlogDetailView.as_view())
# ]
from rest_framework.routers import DefaultRouter
from .views import BlogModelViewSet

router = DefaultRouter()
router.register(r"blog", BlogModelViewSet, basename="blog")
urlpatterns = [] + router.urls
