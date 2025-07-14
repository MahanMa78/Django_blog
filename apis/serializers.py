from rest_framework import serializers
from blog.models import Post
from django.contrib.auth import get_user_model

class SinglePostSerializers(serializers.Serializer):
    title = serializers.CharField(required = True , allow_null = False , allow_blank = False , max_length = 128 )
    photo = serializers.ImageField(required = True ,   allow_null = False , allow_empty_file = False )
    body = serializers.CharField(required = True , allow_null = False , allow_blank = False , max_length = 2048 )
    date = serializers.DateField(required = True , allow_null = False)

    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title' ,'excerpt','body', 'author' , 'photo','category')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",'email' , "first_name" , 'last_name')