from django.urls import path
from .views import (
    HomeView ,
    PostNewView ,
    PostDetailView ,
    PostDeleteView ,
    PostUpdateView ,
    search_view,
    AllPostsAPIView,
)

urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path('search/', search_view, name='search'),
    path("post/new/", PostNewView.as_view() , name='newpost'),
    path('post/<int:pk>/', PostDetailView.as_view()  , name='post_detail'),
    path('post/update/<int:pk>' , PostUpdateView.as_view() , name='update'),
    path('post/delete/<int:pk>/' , PostDeleteView.as_view() , name='delete'),
    path('post/all/' , AllPostsAPIView.as_view() , name='all_posts'),
]
