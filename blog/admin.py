from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Recipe, Comment, Ingredient, PreparationStep, Likes
from django_summernote.admin import SummernoteModelAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'published_on')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'published_on')
    summernote_fields = ('description')


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
