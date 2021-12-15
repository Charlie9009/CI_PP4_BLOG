"""
Import from django and from models module.
"""
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Using ListView to render to the index.html.
    Also filtering so only published posts show up
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
