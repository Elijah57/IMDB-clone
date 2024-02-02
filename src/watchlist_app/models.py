from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=250)
    url = models.URLField()

    class Meta:
        unique_together = ("name", "url")

    def __str__(self):
        return self.name


class Media(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=300)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.SET_NULL, null=True)
    date_released = models.DateTimeField(auto_now_add=True)
    num_rating = models.IntegerField(default=0)
    avg_rating= models.FloatField(default=0)
    active = models.BooleanField()

    def __str__(self):
        return self.name 
    

class Review(models.Model):
    the_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating) + " Star(s)" + str(self.media)
