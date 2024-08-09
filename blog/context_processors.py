from .models import Post

def recent_posts(request):
    recent_posts = Post.objects.order_by('-date')[:5]
    return {'recent_posts' : recent_posts}

#ma dar inja darim query mizanim be data base va yekseri etelaat migirm , hala ba estefade az in etelaat dar dakhel safhe html azash estefadeh mikonim
#chon ma dakhel context_processors in function ro neveshtim dige safhe sidebar.html ma on ro mishnase
