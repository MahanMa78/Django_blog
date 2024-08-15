from django.test import TestCase
from django.shortcuts import reverse #reverse name url ro az ma migire va asl ro be ma barmigardone
from .models import Post
from accounts.models import CustomUser
from django.core.paginator import Paginator


class BlogListViewTest(TestCase):
#dar test nevisi function ha bayad hatman ba "test_" shoro beshan
    def test_blog_list_view_url(self):#in dare ba url test mikone
        response = self.client.get('/') #ba url mire va test haro misanje
        self.assertEqual(response.status_code , 200)

    def test_blog_list_view_url_by_name(self):#in dare ba name url test mikone
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code , 200)

    def test_blog_search_view_url(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code , 200)

    def test_blog_list_pages(self):
        user = CustomUser.objects.create_user(username='mahan', password='password')
        post = Post.objects.create(
                title='post 1' ,
                excerpt = 'some lines' ,
                author = user,
                date = '2024-08-21' , 
                photo = '\media\photo\2024\08\09\Coding_wallpaper_by_Sajas823_-_Download_on_ZEDGE___eacb.jpg',
                active = True,)

        response = self.client.get(reverse('home'))
        self.assertContains(response , 'some lines' )


    def test_blog_detail_view_url(self):
        response = self.client.get('/post/new/')
        self.assertEqual(response.status_code , 200)

    
    def test_blog_detail_page(self):
        user = CustomUser.objects.create_user(username='mahan', password='password')
        post = Post.objects.create(
                title='post 1' ,
                excerpt = 'some lines' ,
                body = 'more lines',
                author = user,
                date = '2024-08-21' , 
                photo = '\media\photo\2024\08\09\Coding_wallpaper_by_Sajas823_-_Download_on_ZEDGE___eacb.jpg',
                active = True,)
        
        response = self.client.get(reverse('post_detail', kwargs={'pk': post.pk}))
        self.assertContains(response , 'more lines')