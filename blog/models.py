from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    DJANGO = 'DJ'
    PYTHON = 'PY'
    GIT = 'GIT'
    HTTML = 'HTML'
    PHOTOSHOP = 'PS'
    PLACE_TYPE_CHOICES = (
        (DJANGO, 'DJANGO'),
        (PYTHON, 'PYTHON'),
        (GIT, 'GIT'),
        (HTTML, 'HTML'),
        (PHOTOSHOP, 'PHOTOSHOP'),
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=PLACE_TYPE_CHOICES, null=True, blank=True)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True

        self.save()

    def __str__(self):
        return self.text



