"""
Imports from django
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create a constant tuple to make sure if a post is in draft or published
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Create a post model to be able to post on the site
    with relevant variables
    """
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def get_absolute_url(self):
        """
        Get absolute url for specific posts
        """
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Create a comment model to be able to comment on posts with names and text.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='name'
        )
    body = models.TextField(max_length=130, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

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


class Question(models.Model):
    """
    Create a model for a questions page
    """
    title = models.CharField(max_length=100)
    question = models.TextField(max_length=200)
    answer = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    answered_on = models.BooleanField(default=False)

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
