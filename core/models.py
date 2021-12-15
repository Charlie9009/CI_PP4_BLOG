"""
Imports from django
"""
from django.db import models
from django.contrib.auth.models import User

# Create a constant tuple to make sure if a post is in draft or published
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Create a post model to be able to post on the site.
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Create a comment model to be able to comment on posts with names and text.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
