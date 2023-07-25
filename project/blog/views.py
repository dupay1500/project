from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Category

# Create your views here.

def index(request):
    articles = Article.objects.all()
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        "title": "Maqolalar ro'yxati",
        # 'categories': categories
    }
    return render(request, 'blog/all_articles.html', context)


def category_list(request, pk):
    articles = Article.objects.filter(category_id=pk)
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        # 'categories': categories
    }
    return render(request, "blog/all_articles.html", context)