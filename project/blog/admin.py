from django.contrib import admin
from .models import Article, Category, User

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'updated_at', 'view', 'author', 'category', 'is_published')
    list_display_links = ('title',)
    list_editable = ('author', 'category', 'is_published')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(User)