from django.contrib import admin
from .models import Post , Comment , Category , AboutContactUs


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title' , 'photo']

admin.site.register(Category , CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'author'  , 'category' , 'date' , 'active' ,'comments_count']
    list_per_page = 5 #mige dar har safhe az pannel admin chanta neshon bede
    ordering = ['-date']
#baraye zamani ke ma yek field dakhel model aslimon nadarim vali mikhahim on ro namayesh bedim on ro minevism va baadesh tarifesh mikonim(be sorat yek function) 
admin.site.register(Post , PostAdmin)

admin.site.register(Comment)
admin.site.register(AboutContactUs)