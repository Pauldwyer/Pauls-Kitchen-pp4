from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


# Custom User Model
class CustomUser(AbstractUser):
    pass
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


# Recipe Model
class Recipe(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(null=True)
    preparation_steps = models.TextField(null=True)
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(CustomUser, related_name='liked_recipe')

    class Meta:
        """
        Order
        """
        ordering = ['-published_on']

    def __str__(self):
        return self.title


# Comments Model
class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
