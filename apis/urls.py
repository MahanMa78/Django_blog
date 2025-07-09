from django.urls import path
from .views import AllPostsAPIView , SinglePostAPIView , SearchPostAPIView 


urlpatterns = [
    path('post/all/' , AllPostsAPIView.as_view() , name='all_posts'),
    path('post/' , SinglePostAPIView.as_view() , name='single_post'),
    # path('post/<int:pk>/' , PostAPIView.as_view() , name='post_title'),
    path('post/search/' , SearchPostAPIView.as_view() , name='search_post'),
]
