from django.db import models

from account.models import SiteUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

# shim


class Reply(models.Model):
    post = models.ForiegnKey(Post, null=True, blank=True)
    author = models.ForiegnKey(SiteUser, null=True, blank=True)



