from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Reviews(models.Model):
    movie_title = models.CharField(max_length=255)
    content_review = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_created_at = models.DateTimeField(auto_now_add=True)
    review_score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), 
            MaxValueValidator(5)])

    def __str__(self):
        return f"{self.movie_title} - {self.user.username} - {self.review_score}"