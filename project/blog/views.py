from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Article, Category, User
from .forms import ArticleForm

# Create your views here.

class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    # template_name = 'blog/all_articles.html'
    extra_context = {
        'title': "Maqolalar ro'yxati"
    }

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class ArticleDetail(DetailView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = Article.objects.get(pk=self.kwargs['pk']).title
        return context


class NewArticle(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    extra_context = {
        'title': "class yordamnida ma'qola qo'shish"
    }
    success_url = reverse_lazy('index')


class ArticleListByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListByCategory, self).get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


class SearchResults(ArticleList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(title__contains=word)
        return articles


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('index')



def profile(request):
    if request.user.is_authenticated:
        user_id = request.user.pk
        user = User.objects.get(pk=user_id)

        context = {
            'title': "Sizning profilingiz!",
            'user': user
        }

        return render(request, "blog/profile.html", context)
    else:
        return HttpResponse("Saytga kir Bratishka😡")








# def index(request):
#     articles = Article.objects.filter(is_published=True)
#     # categories = Category.objects.all()
#     context = {
#         'articles': articles,
#         "title": "Maqolalar ro'yxati",
#         # 'categories': categories
#     }
#     return render(request, 'blog/all_articles.html', context)


# def category_list(request, pk):
#     articles = Article.objects.filter(category_id=pk, is_published=True)
#     # categories = Category.objects.all()
#     context = {
#         'articles': articles,
#         # 'categories': categories
#     }
#     return render(request, "blog/all_articles.html", context)


# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk, is_published=True)
#     context = {
#         'title': "Maqola",
#         'article': article
#     }
#     return render(request, 'blog/detail.html', context)


# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             article = Article.objects.create(**form.cleaned_data)
#             article.save()
#             return redirect('article_detail', article.pk)
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form,
#         'title': "Maqola qo'shish"
#     }
#     return render(request, 'blog/article_form.html', context)