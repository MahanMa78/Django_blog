from django.contrib import admin
from .models import Post , Comment , Categroy


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title' , 'photo']

admin.site.register(Categroy , CategoryAdmin)


admin.site.register(Post)
admin.site.register(Comment)