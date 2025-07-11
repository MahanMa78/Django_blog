from django.urls import path
from .views import AllPostsAPIView , SinglePostAPIView , SearchPostAPIView , PostAPIView


urlpatterns = [
    # path('' , ListAPIView.as_view() , name='post_list'),
    path('post/all/' , AllPostsAPIView.as_view() , name='all_posts'),
    path('post/' , SinglePostAPIView.as_view() , name='single_post'),#baraye zamani ke bekhahim ba title yek post ro peyda konim --> ?post_title= bayad in ro bezarim
    path('post/<int:pk>/' , PostAPIView.as_view() , name='post_title'),
    path('post/search/' , SearchPostAPIView.as_view() , name='search_post'),
]
