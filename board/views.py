from django.shortcuts import render
from board.models import Board, Category
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from board.forms import BoardForm
# Create your views here.
def post_list(request):
    ctg = request.GET.get("category")
    if ctg == 'news':
        boards = Board.objects.filter(category = 2)
    elif ctg == 'free':
        boards = Board.objects.filter(category = 1)
    else:
        boards = Board.objects.all()

    return render(request, 'board/post_list.html', {'boards': boards, 'ctg': ctg})






# @login_required
# def post_list(request, ctg):
#     ctgr = Category.objects.all()
#     if ctg == 'news':
#         boards = Board.objects.filter(category = 2)
#     elif ctg == 'free':
#         boards = Board.objects.filter(category = 1)
#     else:
#         boards = Board.objects.all()
#
#     return render(request, 'board/post_list.html', {'boards': boards, 'ctgr': ctgr})



def post_detail(request, pk):
    ctgr = Category.objects.all()
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/post_detail.html', {'board': board})

@login_required
def post_new(request):

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()

    return render(request, 'board/post_edit.html', {'form': form})

def post_edit(request, pk):

    post = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('Board:post_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)

    return render(request, 'Board/post_edit.html', {'form': form})