from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    view = models.IntegerField(default=0, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)