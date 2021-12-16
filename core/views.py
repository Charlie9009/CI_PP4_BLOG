"""
Import from django and from models module.
"""
from django.views import generic, View
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Using ListView to render to the index.html.
    Also filtering so only published posts show up
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(View):
    """
    This class 'PostDetail' is taken from Code Institutes school project 'DjangoBlog'
    and altered slightly for this project.
    It is added so that a user can comment on the page
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('created_on')
        

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm()
            },
        )


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return search_list
