from django.db import models
from django.conf import settings


# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.FloatField()
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="review/", blank=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
