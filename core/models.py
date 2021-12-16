"""
Imports from django
"""
from django.db import models
from django.contrib.auth.models import User

# Create a constant tuple to make sure if a post is in draft or published
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Create a post model to be able to post on the site
    with relevant variables
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Order by descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Return title string
        """
        return self.title


class Comment(models.Model):
    """
    Create a comment model to be able to comment on posts with names and text.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """
        Order by descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns an f string of a comments body and name
        """
        return f'Comment {self.body} by {self.name}'
