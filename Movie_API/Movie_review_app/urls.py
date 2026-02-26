from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewsViewSet, UserViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewsViewSet, basename='reviews')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
