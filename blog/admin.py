from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Post , Comment , Category , AboutContactUs
from django.db.models import Count



class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title' , 'photo']
    # list_filter

admin.site.register(Category , CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'author'  , 'category' , 'date' , 'active' ,'comments_count']
    list_per_page = 5 #mige dar har safhe az pannel admin chanta neshon bede
    ordering = ['-date'] #bar asas date miad va sort mikone
    list_select_related = ['category'] #baraye behine kardan queryset ha
    list_filter = ['date' , 'category' ,] #filter haye kenar pannel admin bar asas in ha hastan
    search_fields = ['title' , 'author__username' ,] #be vasile inha miad va search mikone
    list_display_links =['id','title','author']

    def get_queryset(self, request):
        return super().get_queryset(request)\
            .prefetch_related('comment')\
            .annotate(
                comments_count = Count('comment'),
            )

    @admin.display(description='# commetns' , ordering='comments_count')
    def comments_count(self , post :Post):
        return post.comments_count
#baraye zamani ke ma yek field dakhel model aslimon nadarim vali mikhahim on ro namayesh bedim on ro minevism va baadesh tarifesh mikonim(be sorat yek function) 
admin.site.register(Post , PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'author' , 'date' , 'active' , 'post']
    list_editable = ['active']
    list_per_page = 10
    list_filter = ['date']
admin.site.register(Comment , CommentAdmin)

admin.site.register(AboutContactUs)