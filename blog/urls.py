from django.urls import path
from .views import (
    HomeView ,
    PostNewView ,
    PostDetailView ,
    PostDeleteView ,
    PostUpdateView ,
    search_view,
    AllPostsAPIView,
    SinglePostAPIView,
    SearchPostAPIView,
    AboutUsView,
    ContactUs,
    TermsOfServicesView,
    PrivacyPolicyView,
)

urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path('search/', search_view, name='search'),
    path("post/new/", PostNewView.as_view() , name='newpost'),
    path('post/<int:pk>/', PostDetailView.as_view()  , name='post_detail'),
    path('post/update/<int:pk>' , PostUpdateView.as_view() , name='update'),
    path('post/delete/<int:pk>/' , PostDeleteView.as_view() , name='delete'),
    path('post/all/' , AllPostsAPIView.as_view() , name='all_posts'),
    path('post/' , SinglePostAPIView.as_view() , name='single_post'),
    path('post/search/' , SearchPostAPIView.as_view() , name='search_post'),
    path('aboutus/', AboutUsView.as_view() ,name='aboutus'),
    path('contactus/', ContactUs.as_view() ,name='contactus'),
    path('terms/' , TermsOfServicesView.as_view() , name='terms'),
    path('policy/' , PrivacyPolicyView.as_view() , name='policy'),
    
]
