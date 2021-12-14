from django.contrib import admin
from .models import Post


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
