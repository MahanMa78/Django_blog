from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

#ma ta ghabl az merge kardan commit ha bedon model baraye khodemon mitonestim yek user besazim
#ama az inja be baad ma user ro shakhsi saz tar kardim

class CustomUser(AbstractUser):
    birth_date = models.DateField(null = True , blank=True)
    photo = models.ImageField(upload_to='photo/profile/%Y/%m/%d/' , default='null')
    about = models.CharField(max_length=255 , default='null') 
    #default='null' --> komak mikone ke data haye ghabli dakhel database zamani ke vojod daran dochar moshkel nashan
    description = RichTextField(default='something about me')