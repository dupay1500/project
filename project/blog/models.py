from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse, reverse_lazy

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Maqola nomi")
    content = models.TextField(blank=True, verbose_name="Matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuklangan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Rasmi")
    is_published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    view = models.IntegerField(default=0, blank=True, null=True, verbose_name="Ko'rishlar soni")
    author = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Muallif")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriyasi")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        # ordering = ['-created_at']


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    status = models.CharField(max_length=75, blank=True, null=True, verbose_name="Darajasi")
    address = models.CharField(max_length=250, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=18, blank=True, null=True)