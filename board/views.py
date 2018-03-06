from django.shortcuts import render
from board.models import Board, Category
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from board.models import File, Image

from board.forms import BoardForm, FileForm, ImageForm
# Create your views here.
def post_list(request):
    category = request.GET.get("category")
    if category != None:

        boards = Board.objects.filter(category__name = category)

    else:
        boards = Board.objects.all()

    category = Category.objects.all()
    return render(request, 'board/post_list.html', {'boards': boards, 'categolies': category})





# 캐릭터필드를 이용했을 때
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

    board = get_object_or_404(Board, pk=pk)
    files = board.file_set.all()
    images = board.image_set.all()


    return render(request, 'board/post_detail.html', {'board': board, 'files': files, 'images': images})

@login_required
def post_new(request):

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            upfls = request.FILES.getlist('file')
            for upfl in upfls:
                file = File()
                file.file = upfl
                file.post = post
                file.save()

            upimgs = request.FILES.getlist('image')
            for upimg in upimgs:
                img = Image()
                img.image = upimg
                img.post = post
                img.save()



            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()
        file = FileForm()
        image = ImageForm()

    return render(request, 'board/post_edit.html', {'form': form,'file': file, 'image': image})


def post_edit(request, pk):

    post = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)

    return render(request, 'board/post_edit.html', {'form': form})

def post_remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board:post_list')

