from django.shortcuts import render
from .models import Reviews
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters
from .Serializers import ReviewsSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['review_score', 'review_created_at']
    search_fields = ['movie_title', 'content_review']

    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





