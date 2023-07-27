from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article, Category

# Create your views here.

def index(request):
    articles = Article.objects.filter(is_published=True)
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        "title": "Maqolalar ro'yxati",
        # 'categories': categories
    }
    return render(request, 'blog/all_articles.html', context)


def category_list(request, pk):
    articles = Article.objects.filter(category_id=pk, is_published=True)
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        # 'categories': categories
    }
    return render(request, "blog/all_articles.html", context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    context = {
        'title': "Maqola",
        'article': article
    }
    return render(request, 'blog/detail.html', context)