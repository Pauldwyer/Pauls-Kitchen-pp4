from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


# Recipe table
class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes')
    preparation_steps = models.ManyToManyField('PreparationStep', related_name='recipes')

    class Meta:
        """
        Order
        """
        ordering = ['-published_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PreparationStep(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Likes(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} likes {self.post}'


# Create your models here.
