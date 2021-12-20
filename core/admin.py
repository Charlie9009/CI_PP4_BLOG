"""
Import from django and from models module
"""
from django.contrib import admin
from .models import Post, Comment, Questions


class PostAdmin(admin.ModelAdmin):
    """
    Create class and variables to make reading, finding, searching
    and filtering posts easier
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


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


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):     
    list_display = ('title', 'question', 'answer', 'created_on', 'answered_on')
    list_filter = ('title', 'question', 'answer', 'created_on', 'answered_on')
    search_fields = ('title', 'question', 'created_on', 'answered_on')
    actions = ('answered_on')
