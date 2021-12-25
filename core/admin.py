"""
Import from django and from models module
"""
from django.contrib import admin
from .models import Post, Comment, Question


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Create class and variables to make reading, finding, searching
    and filtering posts easier
    """
    list_display = ('title', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Create class and variables to make comments and info about the comments
    visible to the admin
    """
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Create class and variables to make reading, finding, searching
    and filtering questions easier
    """
    list_display = ('title', 'question', 'answer', 'created_on', 'answered_on')
    list_filter = ('title', 'question', 'answer', 'created_on', 'answered_on')
    search_fields = ('title', 'question', 'created_on', 'answered_on')
    actions = ('answered_on')
