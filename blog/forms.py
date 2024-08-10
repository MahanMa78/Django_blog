from django import forms
from .models import Post , Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'excerpt' , 'body'  , 'date' , 'photo'] # ma 'author' ro hazf kardim ta mostaghiman khode on kasi ke dare post ro minevise biad va post ro montasher kone
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'excerpt' , 'body' , 'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']