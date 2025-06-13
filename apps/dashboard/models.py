from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='post_images/')
    title = models.TextField(max_length=255,blank=True,null=True)
    context = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
