from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.views import LogoutView

admin.site.site_header = 'Blog' #miad va esme Django Adminstration ro taghir mide
admin.site.index_title = 'Special Access' #miad va esme Site administration ro taghir mide



schema_view = get_schema_view(
   openapi.Info(
      title="Todo API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('blog.urls')),
    path('accounts/' , include('django.contrib.auth.urls')),#in faghat baraye login va logout kar mikone
    #ma bayad yek folder dar templates/registraion besazim
    path('accounts/' , include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/' , include("apis.urls")),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
