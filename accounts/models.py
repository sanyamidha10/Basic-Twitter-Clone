from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(default='')

    def __str__(self):
        return self.user.username