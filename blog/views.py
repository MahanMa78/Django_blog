from django.http import HttpRequest, HttpResponse
from django.views.generic import  CreateView , DetailView , DeleteView ,ListView , View , FormView
from django.views.generic.edit import UpdateView , DeleteView
from .models import Post
from .forms import PostForm , PostUpdateForm , CommentForm , SearchForm
from django.urls import reverse_lazy , reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin #be vasile in mohtavaye ke behesh atach shode be yek url ro estekhraj mikonim
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HomeView(View): #bayad az ListView be View taghir bedim
    # model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 1 #manzor tedad post hay ke dakhel yek safhe mishe did

    def get(self, request):
        posts = Post.objects.filter(active= True)
        paginator = Paginator(posts,self.paginate_by) #tamam safahat dakhelsh hast va har safhe ham tedadi post dakhelesh dare

        page_number = request.GET.get('page') #pagi ke karbar mikhad estekhraj beshe
        page_obj = paginator.get_page(page_number) #shomare pagi ke karbar mikhad ro estekhraj kon va beriz dakhel page_obj

        context = {
            'post_list' : page_obj, #ma on pagi ke mored nazar karbar hast ro rikhtim dakhel post_list
        }

        return render(request , self.template_name , context) #manzor inke boro to template ke man mikham va be hamrah mohtavie ke man behet midam
    


class PostNewView(CreateView):
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
        context['form'] = CommentForm()
        return context


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


class PostDetailView(View):
    def get(self, request , *args , **kwargs):
        view = CommentGet.as_view()
        return view(request , *args , **kwargs)
    
    def post(self, request , *args , **kwargs):
        view = CommentPost.as_view()
        return view(request , *args , **kwargs)


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostUpdateForm
    # fileds = ['title' , 'excerpt' , 'body' , 'photo']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

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


class AllPostsAPIView(APIView):

    def get(self , request ,format = None):
        try:
            all_posts = Post.objects.filter(active = True).order_by('-date')[:10]
            data = []
            for post in all_posts:
                data.append({
                    'title' : post.title,
                    'excerpt' : post.excerpt,
                    'body' : post.body ,
                    'author' : post.author.username ,
                    'date' : post.date ,
                    'photo' : post.photo.url if post.photo else None , 
                    'category' : {
                        'id': post.category.id if post.category else None,
                        'title': post.category.title if post.category else None,
                    }, 
                    'tags': [tag.name for tag in post.tags.all()],
                })

            return Response({'data': data } , status=status.HTTP_200_OK)
        except:
            return Response({'status' : "Internal Server Error  , We'll Check It Latter"},
                            status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        