from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


# Comments table
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} on {self.post}'


# Recipe table
class Recipe(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    published_on = models.DateTimeField()
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    ingredients = models.ManyToManyField('Ingredient')
    preparation_steps = models.ManyToManyField('PreparationStep')

    class Meta:
        """
        Order
        """
        ordering = ['-published_on']

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class PreparationStep(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    port = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f'{self.user} likes {self.post}'


# Create your models here.
