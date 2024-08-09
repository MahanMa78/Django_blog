from django.urls import path
from .views import (
    HomeView ,
    PostNewView ,
    PostDetailView ,
    PostDeleteView ,
    PostUpdateView ,
 
    
)

urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path("post/new/", PostNewView.as_view() , name='newpost'),
    path('post/<int:pk>/', PostDetailView.as_view()  , name='post_detail'),
    path('post/update/<int:pk>' , PostUpdateView.as_view() , name='update'),
    path('post/delete/<int:pk>/' , PostDeleteView.as_view() , name='delete'),

]
