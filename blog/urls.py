from django.urls import path
from . import views

from .views import SignUpView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('', views.RecipeList.as_view(), name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('recipe_list', views.RecipeList.as_view(), name='recipe_list'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]