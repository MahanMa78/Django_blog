from django.db import models
from django.contrib.auth.models import AbstractUser

#ma ta ghabl az merge kardan commit ha bedon model baraye khodemon mitonestim yek user besazim
#ama az inja be baad ma user ro shakhsi saz tar kardim

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null = True , blank=True)
