"""
Import from django, models module and from forms module.
"""
from django.views import generic, View
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Question, Comment
from .forms import CommentForm


class PostList(ListView):
    """
    Using ListView to render to the index.html.
    Also filtering so only published posts show up
    """
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_on']


class PostDetail(View):
    """
    This class 'PostDetail' was first taken from Code Institutes school project
    'DjangoBlog'
    and then reworked a bit for this project.
    It is added so that a user can get the posts displayed and be able
    to make a comment
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'post_detail.html', context)


    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.name = request.user
            comment.post = post
            comment.save()
        
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'post_detail.html', context)



class SearchResultsView(generic.ListView):
    """
    Setting up class to add search function to the site
    Getting the model 'Post' and the template 'search_results'
    """
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        """
        Setting up a query to search for the users input
        and filter them with Q objects by 'title' and 'content'
        """
        query = self.request.GET.get('q')
        search_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return search_list


class QuestionView(generic.ListView):
    queryset = Question.objects.filter(answered_on=True).order_by('-answered_on')
    template_name = 'question.html'
