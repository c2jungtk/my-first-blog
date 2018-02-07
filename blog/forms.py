from django import forms
from blog.models import Post

# class Postform(forms.Form):
#     title = forms.CharField(max_length=200)
#     text = forms.Textarea()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)