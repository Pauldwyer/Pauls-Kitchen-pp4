from django.urls import path
from . import views

from .views import SignUpView, AddRecipeView, RecipeDetail, RecipeLike, ProfileView, EditRecipeView, DeleteRecipeView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('recipe_list', views.RecipeList.as_view(), name='recipe_list'),
    path('add_recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('my_profile/', ProfileView.as_view(), name='my_profile'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='like_recipe'),
    path('recipe/<slug:slug>/edit/', EditRecipeView.as_view(), name='edit_recipe'),
    path('recipe/<slug:slug>/delete/', DeleteRecipeView.as_view(), name='delete_recipe'),
]
