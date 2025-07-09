from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.generic import  CreateView , DetailView , DeleteView ,TemplateView , View , FormView
from django.views.generic.edit import UpdateView , DeleteView
from .models import Category, Post , AboutContactUs , Comment , Reply, TermsOfServices , PrivacyPolicy
from .forms import PostForm , PostUpdateForm , CommentForm , SearchForm , ReplyCreateForm
from django.urls import reverse_lazy , reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import SingleObjectMixin #be vasile in mohtavaye ke behesh atach shode be yek url ro estekhraj mikonim
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .apis import serializers
from django.conf import settings
from accounts.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

class HomeView(View): #bayad az ListView be View taghir bedim
    # model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 3 #manzor tedad post hay ke dakhel yek safhe mishe did

    def get(self, request):
        posts = Post.objects.filter(active= True).order_by('-date')
        paginator = Paginator(posts,self.paginate_by) #tamam safahat dakhelsh hast va har safhe ham tedadi post dakhelesh dare

        page_number = request.GET.get('page') #pagi ke karbar mikhad estekhraj beshe
        page_obj = paginator.get_page(page_number) #shomare pagi ke karbar mikhad ro estekhraj kon va beriz dakhel page_obj

        context = {
            'post_list' : page_obj, #ma on pagi ke mored nazar karbar hast ro rikhtim dakhel post_list
        }

        return render(request , self.template_name , context) #manzor inke boro to template ke man mikham va be hamrah mohtavie ke man behet midam
    


class CategoryListView(View):
    context_object_name = 'categories'
    def get(self , request):
        categories = Category.objects.all()        
        context = {
        'categories' : categories,
        }
        
        return render(request, 'category_list.html' , context)


class CategoryDetailView(View):
    pass

class PostNewView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm #mishe jash nevesht --> fields = ['title' , 'excerpt' , 'body' , 'autthor' , 'date' , 'photo']
    success_url = reverse_lazy('home')
    template_name = 'post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #in ham mishe jaye success_url nevesht
    # def get_success_url(self):
    #     return reverse_lazy('home')


#ma bayad yek bar baraye get request class benevisim va yek bar baraye post request
class CommentGet(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm() 
        context['reply_form'] = ReplyCreateForm() 
        return context


class ReplyPost(SingleObjectMixin , FormView):
    model = Comment
    form_class = ReplyCreateForm
    template_name = 'post_detail.html'

    def post(self , request , *args , **kwargs):
        self.object = self.get_object()
        return super().post(request , *args , **kwargs)
    
    def form_valid(self, form):
        reply = form.save(commit = False)
        parent_comment_id = self.request.POST.get("parent_comment_id")
        parent_comment = Comment.objects.get(id=parent_comment_id)
        reply.parent_comment = parent_comment
        reply.author = self.request.user
        reply.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.object.post
        return reverse('post_detail' , kwargs={'pk' : post.pk})
    

# ma ham be SingleObjectMixin niaz darim va ham be FormView ta Form ro ersal konim
class CommentPost(SingleObjectMixin , FormView):
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'

    def post(self , request , *args , **kwargs ):
        self.object = self.get_object() #get_object() az SingleObjectMixin miad va mire post feli ro baraye man kolan estekhraj mikone va baraye man miare
        return super().post(request,*args, **kwargs)
    
    def form_valid(self ,form ): #miad form ro ke az samte karbar miad ro check mikone
        comment = form.save(commit = False) #manzor az commit = False inke felan dakhel database zakhire nmishe
        comment.post = self.object
        comment.author = self.request.user        
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail' , kwargs={'pk' : post.pk})


class PostDetailView(LoginRequiredMixin,View):
    def get(self, request , *args , **kwargs):
        view = CommentGet.as_view()
        return view(request , *args , **kwargs)
    
    def post(self, request , *args , **kwargs):
        if 'parent_comment_id' in request.POST:
            view = ReplyPost.as_view()
        else:
            view = CommentPost.as_view()
        return view(request , *args , **kwargs)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostUpdateForm
    # fileds = ['title' , 'excerpt' , 'body' , 'photo']
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user  # check if the user is the author of the

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

def search_view(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(title__icontains=query)  # جستجو در عنوان پست‌ها

    return render(request, 'search_results.html', {'form': form, 'query': query, 'results': results})

       

# def about_us(request):
#     admin_users = CustomUser.objects.filter(is_superuser=True)
#     text = """
#         Welcome to our website. Here is some information about us and our admin team:
#     """
#     context = {
#         'admin_users': admin_users,
#         'text' : text,
#     }
#     return render(request, 'aboutus.html', context)


class AboutUsView(TemplateView):
    # model = AboutContactUs
    template_name = 'aboutus.html'
    # context_object_name = 'about_us'
    

    def get(self, request):
        admin_users = CustomUser.objects.filter(is_superuser=True)
        aboutus = AboutContactUs.objects.first()
        context = {
            'admin_users' : admin_users,
            'about_us' : aboutus,
        }
        return render(request , self.template_name , context)
    


# def contact_us(request):
#     contact_info = """
#         our connecting links
# """
#     email = 'mahan@blog.com'

#     context ={
#         'contact_info' : contact_info,
#         'email' : email,
#     }

#     return render(request , 'contactus.html' , context)

class ContactUsView(TemplateView):
    template_name = 'contactus.html'
    
    def get(self, request):
        contactus = AboutContactUs.objects.first()
        context = {
            'contact_us' : contactus,
        }
        return render(request , self.template_name , context)
    
class TermsOfServicesView(TemplateView):
    template_name = 'terms.html'
    
    def get(self , request):
        terms = TermsOfServices.objects.first()
        context = {
            'terms' : terms,
        }
        return render(request , self.template_name , context)
    
class PrivacyPolicyView(TemplateView):
    template_name = 'policy.html'
    
    def get(self , request):
        privacy = PrivacyPolicy.objects.first()
        context = {
            'privacy' : privacy,
        }
        return render(request , self.template_name , context)