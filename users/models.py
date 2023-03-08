from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    register_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(blank=True, null=True, default='avatar.jpg')
    full_name = models.CharField(max_length=255)


def __str_(self):
    return self.full_name
