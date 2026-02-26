from django.shortcuts import render
from .models import Reviews, User
from rest_framework import viewsets, permissions
from .Serializers import ReviewsSerializer, UserSerializer
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





