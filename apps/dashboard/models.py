from django.db import models
import uuid
# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    title = models.TextField(max_length=255,blank=True,null=True)
    context = models.TextField(max_length=255,blank=True,null=True)
    is_active = models.BooleanField(default=True)

class BaseClass(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,primary_key=True,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class User(BaseClass):
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    is_active=models.BooleanField(default=False)