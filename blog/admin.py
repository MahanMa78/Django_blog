from django.contrib import admin
from .models import Post , Comment , Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title' , 'photo']

admin.site.register(Category , CategoryAdmin)


admin.site.register(Post)
admin.site.register(Comment)