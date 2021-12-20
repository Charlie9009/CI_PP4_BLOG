"""
Import from django, models module and from forms module.
"""
from django.views import generic, View
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Question
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
    This class 'PostDetail' is taken from Code Institutes school project
    'DjangoBlog'
    and altered slightly for this project.
    It is added so that a user can comment on the page
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Create function to filter the query of active posts and comments
        and render them to the user.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('-created_on')

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
        """
        Create function to filter the query of active posts and comments
        Also if a user commented successfully on the page that comment is
        saved to the site
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(active=True).order_by('-created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user
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
    model = Question
    template_name = 'questions.html'
