from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_description = models.TextField(blank=True)
    movie_release_date = models.DateTimeField(auto_now_add=True)
    movie_post_URL = models.URLField(blank=True, null=True)
    


class Rating(models.Model):
    movie_title = models.OneToOneField(Movie, on_delete=models.CASCADE)
    movie_score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), 
            MaxValueValidator(5)])

class Reviews(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content_review = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_created_at = models.DateTimeField(auto_now_add=True)
    review_score = models.OneToOneField(Rating, on_delete=models.CASCADE)

