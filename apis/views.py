from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from blog.models import Post

class AllPostsAPIView(APIView):
# baraye search kardanesh bayad benevisim : http://localhost:8000/post/all/
    def get(self , request ,format = None):
        try:
            all_posts = Post.objects.filter(active = True).order_by('-date')[:10]
            data = []
            for post in all_posts:
                data.append({
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
        
  

class SinglePostAPIView(APIView):#baraye zamani estefade mishe ke bekhahim yek maghale ro search konim
 # baraye search kardanesh bayad benevisim : http://localhost:8000/post/?post_title=
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