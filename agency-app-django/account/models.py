from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="user", default="user/user.png")
    bio = models.TextField(null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    auth_token = models.CharField(max_length=120)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name
