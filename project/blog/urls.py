from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    # path('category/<int:pk>/', category_list, name='category_list'),
    # path('article/<int:pk>/', article_detail, name='article_detail'),
    # path('add/', add_article, name='lyuboy'),

    path('', ArticleList.as_view(), name='index'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('new/', NewArticle.as_view(), name='lyuboy'),
    path('category/<int:pk>/', ArticleListByCategory.as_view(), name='category_list'),
    path('search/', SearchResults.as_view(), name='search_results'),
    path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

    path('profile/', profile, name='profile'),
]
