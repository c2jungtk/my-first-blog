from django.contrib import admin
from board.models import Board, Category, File, Image

# Register your models here.
admin.site.register(Board)
admin.site.register(Category)
admin.site.register(File)
admin.site.register(Image)
