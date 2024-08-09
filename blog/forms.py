from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'excerpt' , 'body' , 'author' , 'date' , 'photo']
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'excerpt' , 'body' , 'photo']