from django.urls import path
from .views import (
    HomeView ,
    PostNewView ,
    PostDetailView ,
    PostDeleteView ,
    PostUpdateView ,
    search_view,
    AboutUsView,
    ContactUsView,
    TermsOfServicesView,
    PrivacyPolicyView,
    CategoryListView,
    CategoryDetailView,
)

urlpatterns = [
    path('' , HomeView.as_view() , name='home'),
    path('search/', search_view, name='search'),
    path("post/new/", PostNewView.as_view() , name='newpost'),
    path('post/<int:pk>/', PostDetailView.as_view()  , name='post_detail'),
    path('post/update/<int:pk>' , PostUpdateView.as_view() , name='update'),
    path('post/delete/<int:pk>/' , PostDeleteView.as_view() , name='delete'),
    path('aboutus/', AboutUsView.as_view() ,name='aboutus'),
    path('contactus/', ContactUsView.as_view() ,name='contactus'),
    path('terms/' , TermsOfServicesView.as_view() , name='terms'),
    path('policy/' , PrivacyPolicyView.as_view() , name='policy'),
    path('categories/' , CategoryListView.as_view() , name='categories'),
    path('categories/<int:pk>/' , CategoryDetailView.as_view() , name='category_detail'),
]
