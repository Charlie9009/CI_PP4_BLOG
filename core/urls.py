"""
Import from django and from views module
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
]
