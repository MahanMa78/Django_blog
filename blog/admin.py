from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Post , Comment , Category , AboutContactUs , Reply
from django.db.models import Count , Q
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title' , 'photo']
    # list_filter

admin.site.register(Category , CategoryAdmin)

class CommentInLine(admin.StackedInline):
    model = Comment
    fields = ['author' , 'body' , 'date' , 'active']
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'author'  , 'category' , 'date' , 'active' ,'comments_count']
    list_per_page = 5 #mige dar har safhe az pannel admin chanta neshon bede
    ordering = ['-date'] #bar asas date miad va sort mikone
    list_select_related = ['category'] #baraye behine kardan queryset ha
    list_filter = ['date' , 'category' ,] #filter haye kenar pannel admin bar asas in ha hastan
    search_fields = ['title' , 'author__username' ,] #be vasile inha miad va search mikone
    list_display_links =['id','title',]
    inlines = [CommentInLine]

    def get_queryset(self, request):
        return super().get_queryset(request)\
            .prefetch_related('comment_set')\
            .annotate(
                comments_count = Count('comment' , filter=Q(comment__active=True)) ,
            )
            #dar in code , prefetch_related('comment_set') , man chon related_name ro nadam be model Comment pas Django be tor pish farz az comment_set estefade mikone
            #edame: dar kol bedon related_name esme pishfarz ro momkene be sorat esmeclass_set dar nazar begire , baraye motevajeh shodanesh 
    
    @admin.display(description='# commetns' , ordering='comments_count')
    def comments_count(self , post :Post):
        url = (
            reverse('admin:blog_comment_changelist') 
            + '?'
            + urlencode({
                'post__id': post.id, #in url dar kol moadel 'admin/blog/comment/?post__id' hast
            })
        )
        return format_html('<a href="{}">{}</a>',url,post.comments_count) #ma ba in kar be onjae ke mikhahim link mishim
#baraye zamani ke ma yek field dakhel model aslimon nadarim vali mikhahim on ro namayesh bedim on ro minevism va baadesh tarifesh mikonim(be sorat yek function) 
admin.site.register(Post , PostAdmin)

#



class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'author' , 'date' , 'active' , 'post']
    list_editable = ['active']
    list_per_page = 10
    list_filter = ['date']
    autocomplete_fields =['post',] #baraye inke in filed dorost tarif beshe bayad searchfield dar dakhel PostAdmin tarif beshe
admin.site.register(Comment , CommentAdmin)

admin.site.register(AboutContactUs)
admin.site.register(Reply)