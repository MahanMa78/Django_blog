import uuid
from django.db import models
from datetime import date
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils.html import format_html

class Category(models.Model):
    title = models.CharField(max_length=128 ,default=None )
    photo = models.ImageField(upload_to='photo/category_cover/%Y/%m/%d' , null= True , blank= True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = RichTextField()
    body = RichTextField()
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True , related_query_name = 'category_post', related_name='posts')
    tags = TaggableManager()
    active = models.BooleanField(default=True)
    # color_code = models.CharField(max_length=6)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    # def comments_count(self):
    #     return self.comment_set.count() #az in be baad dakhel khode pannel admin query mizanim
    
    # def colored_title(self):
    #     return format_html(
    #         '<span style="color: #{};">{}</span>',
    #         self.color_code,             
    #         self.title ,      
    #         )
    

class ActiveCommentManger(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManger , self).get_queryset().filter(active = True)
    
class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE ,related_name='comments')
    post = models.ForeignKey(Post , on_delete= models.CASCADE )
    body = models.TextField(null=False , blank=False)
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    active_comments_manager = ActiveCommentManger()

    objects = models.Manager() 

    def __str__(self):
        return f'{self.author.username} : {self.body[:30]}'
    
    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"pk": self.pk})
    
    
class AboutContactUs(models.Model):
    about_us = RichTextField()
    contact_us = RichTextField()
    email = models.EmailField(null=False,blank=False)
    phone_number = models.IntegerField(null = False ,blank=False)
    location = models.TextField(default="None")

    def __str__(self):
        return self.email
    

class Reply(models.Model):
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.SET_NULL , null=True , related_name='replies')
    parent_comment = models.ForeignKey(Comment , on_delete=models.CASCADE , related_name='replies')
    body = models.CharField(max_length=512)
    created = models.DateField(auto_now_add=True)
    id = models.CharField(max_length=100 , default=uuid.uuid4 , unique= True , primary_key= True , editable=False)

    def __str__(self):
        return f'{self.author.username} : {self.body[:30]}'
    
    class Meta:
        ordering = ['created']
        
class TermsOfServices(models.Model):
    terms = models.TextField()
    
    def __str__(self):
        return f"{self.terms[:30]}"
    
class PrivacyPolicy(models.Model):
    privacy = models.TextField()
    
    def __str__(self):
        return f"{self.privacy[:30]}"
    
    
class Message(models.Model):
    sender = models.ForeignKey('accounts.CustomUser' , related_name='sent_messages' , on_delete=models.CASCADE)
    receiver =  models.ForeignKey('accounts.CustomUser' , related_name='received_messages' , on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 