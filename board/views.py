from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from board.forms import BoardForm
# Create your views here.
@login_required
def post_list(request):
    boards = Board.objects.all()

    return render(request, 'board/post_list.html', {'boards': boards})

def post_detail(request, pk):
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