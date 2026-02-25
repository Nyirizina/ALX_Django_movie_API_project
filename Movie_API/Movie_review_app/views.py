from django.shortcuts import render
from .models import Reviews
from rest_framework import viewsets
from .Serializers import ReviewsSerializer
from rest_framework import generics

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


