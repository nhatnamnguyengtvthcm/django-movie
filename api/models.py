from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=360)

    # def __str__(self):
    #     return self.title

    def num_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            sum = sum/len(ratings)
        return sum


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)  # check unique user - movie
        index_together = (('user', 'movie'),)

