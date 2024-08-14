from django import forms
from .models import Post , Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'excerpt' , 'body'  , 'date' , 'photo','category' , 'tags'] # ma 'author' ro hazf kardim ta mostaghiman khode on kasi ke dare post ro minevise biad va post ro montasher kone
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'excerpt' , 'body' , 'photo' , 'category' , 'tags' ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)