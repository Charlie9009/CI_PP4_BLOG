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
    path('post/edit/<int:pk>/', views.PostEditView.as_view(), name='edit_detail'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_detail'),
]
