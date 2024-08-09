from django.views.generic import  CreateView , DetailView , DeleteView ,ListView
from django.views.generic.edit import UpdateView , DeleteView
from .models import Post
from .forms import PostForm , PostUpdateForm
from django.urls import reverse_lazy , reverse

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'
    

class PostNewView(CreateView):
    model = Post
    form_class = PostForm #mishe jash nevesht --> fields = ['title' , 'excerpt' , 'body' , 'autthor' , 'date' , 'photo']
    success_url = reverse_lazy('home')
    template_name = 'post_new.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostUpdateForm
    # fileds = ['title' , 'excerpt' , 'body' , 'photo']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')