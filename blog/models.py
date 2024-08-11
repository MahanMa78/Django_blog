from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(max_length=128 ,default=None )
    photo = models.ImageField(upload_to='photo/category_cover/%Y/%m/%d' , null= True , blank= True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True , related_query_name = 'category_post', related_name='posts')
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete= models.CASCADE)
    body = models.TextField(null=False , blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
    