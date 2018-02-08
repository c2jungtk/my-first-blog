from django.contrib import admin
from .models import Post
from .models import Post, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'approved_comment')

class Postadmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'published_date')

# Register your models here.

admin.site.register(Post, Postadmin)
admin.site.register(Comment)