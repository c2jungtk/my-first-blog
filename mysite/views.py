from django.http import HttpResponse
import datetime
from blog.models import Post
from board.models import Board
from django.shortcuts import render

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body><html>"% now
    posts = Post.objects.order_by('-created_date')[0:5]
    boards = Board.objects.order_by('-created_date')[0:5]

    return render(request, 'home.html', {'posts': posts, 'boards': boards} )
