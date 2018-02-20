from django import forms
from board.models import Board, File, Image

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'text', 'category')

class FileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ('file',)

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)