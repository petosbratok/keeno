from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    director = models.CharField(max_length=100, blank=True)
    stars = models.CharField(max_length=200, blank=True)
    country_year = models.CharField(max_length=100, blank=True)
    picture = models.CharField(max_length=200, blank=True)
    genres = models.CharField(max_length=100, blank=True)
    slogan = models.CharField(max_length=200, blank=True)
    trailer_link = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Theater(models.Model):
    title = models.CharField(max_length=100)
    theater_height = models.IntegerField(blank=True)
    theater_width = models.IntegerField(blank=True)
    seats = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    theater = models.ForeignKey(Theater, blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), blank=True, null=True)
    seats_taken = models.TextField(blank=True)


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
