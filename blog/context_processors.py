from .models import Post , Category
from django.db.models import Count

def recent_posts(request):
    recent_posts = Post.objects.order_by('-date')[:5]
    return {'recent_posts' : recent_posts}

#ma dar inja darim query mizanim be data base va yekseri etelaat migirm , hala ba estefade az in etelaat dar dakhel safhe html azash estefadeh mikonim
#chon ma dakhel context_processors in function ro neveshtim dige safhe sidebar.html ma on ro mishnase
#bayad context_processors ro be setting ham ezafe konim


def categories_posts(request):
    categories_posts = Category.objects.order_by('-title')
    return {'categories_posts' : categories_posts}

def count_categories_posts(request):
    count_categories_posts = Category.objects.annotate(post_count=Count('category_post'))
    return {'count_categories_posts' : count_categories_posts}
    