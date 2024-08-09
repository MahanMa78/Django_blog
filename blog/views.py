from django.views.generic import TemplateView , CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy , reverse

class HomeView(TemplateView):
    template_name = 'home.html'

class PostNewView(CreateView):
    model = Post
    form_class = PostForm #mishe jash nevesht --> fields = ['title' , 'excerpt' , 'body' , 'autthor' , 'date' , 'photo']
    success_url = reverse_lazy('home')
    template_name = 'post_new.html'

    # def get_success_url(self):
    #     return reverse('app_name:home')