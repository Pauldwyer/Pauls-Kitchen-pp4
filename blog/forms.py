from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Recipe


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'preparation_steps', 'image']
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'preparation_steps': SummernoteWidget(),
        }
