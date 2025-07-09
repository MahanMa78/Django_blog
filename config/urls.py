from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include

admin.site.site_header = 'Blog' #miad va esme Django Adminstration ro taghir mide
admin.site.index_title = 'Special Access' #miad va esme Site administration ro taghir mide

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('blog.urls')),
    path('accounts/' , include('django.contrib.auth.urls')),#in faghat baraye login va logout kar mikone
    #ma bayad yek folder dar templates/registraion besazim
    path('accounts/' , include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/' , include("apis.urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
