import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    residential_address = models.CharField(max_length=50)

class UserProfile(models.Model):
    Puuid = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=True)
    user = models.OneToOneField( get_user_model(), on_delete=models.CASCADE, editable=False, related_name='profile' )
    phone = models.IntegerField(blank=True, null=True)
    last_seen = models.DateTimeField(auto_now=True, blank=True)
    username = models.CharField(max_length=30, blank=True)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.username}'

