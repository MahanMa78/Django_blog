from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
from . import serializers
from blog.models import Post
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
# *from rest_framework.permissions import IsAdminUser  ----> albate az in ham mishod estefadeh konim vali ma dar in ja az oni ke neveshtim estefaadeh mikonim

from .permissions import IsAuthorOrReadOnly , IsAdminUser 

class AllPostsAPIView(APIView):
# baraye search kardanesh bayad benevisim : http://localhost:8000/post/all/
    permission_classes = (IsAuthorOrReadOnly,)
    def get(self , request ,format = None):
        try:
            all_posts = Post.objects.filter(active = True).order_by('-date')[:10]
            data = []
            for post in all_posts:
                data.append({
                    'id': post.id,
                    'title' : post.title,
                    'excerpt' : post.excerpt,
                    'body' : post.body ,
                    'author' : post.author.username ,
                    'date' : post.date ,
                    'photo' : post.photo.url if post.photo else None , 
                    'category' : {
                        'id': post.category.id if post.category else None,
                        'title': post.category.title if post.category else None,
                    }, 
                    'tags': [tag.name for tag in post.tags.all()],
                })

            return Response({'data': data } , status=status.HTTP_200_OK)
        except:
            return Response({'status' : "Internal Server Error  , We'll Check It Latter"},
                            status = status.HTTP_500_INTERNAL_SERVER_ERROR)

"""
TODO class ListAPIView(generics.ListAPIView): ---> age ListCreateAPIView bezarim ghabeliate sakhtane oist ro ham dare
TODO    queryset = Post.objects.all()
TODO    serializer_class = serializers.PostSerializer        
?---> yek rah dige baraye neveshtan apiview baraye hamaye post ha
"""
class ListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class SinglePostAPIView(APIView):#baraye zamani estefade mishe ke bekhahim yek maghale ro search konim
 # baraye search kardanesh bayad benevisim : http://localhost:8000/post/?post_title=
    permission_classes = (IsAuthorOrReadOnly,)
    def get(self , request , format = None ):
        try:
            post_title = request.GET['post_title']
            post = Post.objects.filter(title__contains = post_title)
            serialized_data = serializers.SinglePostSerializers(post , many = True)
            data = serialized_data.data

            return Response({"data" : data} , status=status.HTTP_200_OK)
        except:
            return Response({"status" : "Internal Server Error"} ,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
# Create your views here.
class SearchPostAPIView(APIView):#baraye zamani estefade mishe ke bekhahim yek kalame ya matn ro dakhele post ha search konim
    # baraye search kardanesh bayad benevisim : http://localhost:8000/post/search/?query=ye chi zi
    permission_classes = (IsAuthorOrReadOnly,)
    def get(self , request , format = None):
        try:
            from django.db.models import Q
            
            query = request.GET['query']
            # posts = Post.objects.filter(Q(content__icontains = query))
            posts = Post.objects.filter(Q(body__icontains = query))
            data =[]
            for post in posts:
                data.append({
                    'title' : post.title,
                    'excpert' : post.excerpt,
                    "photo" : post.photo.url if post.photo else None,
                    'author' : post.author.username,
                    'body' : post.body,
                    'date' : post.date,
                    'category' : {
                        'id' : post.category.id if post.category else None,
                        'title' : post.category.title if post.category else None,
                    },
                    "tags" : [tag.name for tag in post.tags.all()],
                })

                return Response({'data' : data} , status=status.HTTP_200_OK )

        except:
            return Response({'status' : "Iternal Server Error "} , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class PostAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

# @api_view(['GET'])
# def post_detail(request , title):
#     try:
#         post = Post.objects.get(title = title)
#     except Post.DoesNotExist:
#         return Response({"error" : "Post does not exist"})


class UserList(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser , )
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer