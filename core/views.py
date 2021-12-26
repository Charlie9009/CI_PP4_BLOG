"""
Import from django, models module and from forms module.
"""
from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Question, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Using ListView to render to the index.html.
    Also filtering so only published posts show up
    """
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-created_on']


class PostDetail(LoginRequiredMixin, generic.DetailView):
    """
    This class 'PostDetail' was first taken from Code Institutes school project
    'DjangoBlog'
    and then reworked a bit for this project.
    It is added so that a user can get the posts displayed on the post_detail
    page and see comments as well as make comments
    logged in user is required for functionality
    """
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, pk, *args, **kwargs):
        """
        Get posts and comments and show them on post_detail page.
        """
        post = Post.objects.get(pk=pk)
        comment_form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'post_detail.html', context)

    def post(self, request, pk):
        """
        Function for commenting on page.
        """
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


class PostCreate(LoginRequiredMixin, generic.CreateView):
    """
    Get model, template and which fields to use for creating
    posts, logged in user is required for functionality
    """
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'content']
    """
    Set author for form before submit.
    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Get model, template and which fields to use for updating
    posts, logged in user is required for functionality
    """
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']
    """
    Set author for form before submit.
    """
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
    Check if specific post is the authors so they can update
    """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    Get model and which template to use for deleting
    posts, logged in user is required for functionality
    Go back to home page when deleted post
    """
    model = Post
    template_name = 'post_delete_confirm.html'
    success_url = '/'
    """
    Check if specific post is the authors so they can delete
    """
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class SearchResultsView(LoginRequiredMixin, generic.ListView):
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
    """
    Get a queryset of questions and template of question.
    """
    queryset = Question.objects.filter(
        answered_on=True).order_by('-created_on')
    template_name = 'question.html'
