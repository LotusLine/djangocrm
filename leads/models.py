from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass


class Leads(models.Model):

    SOURCE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age= models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
