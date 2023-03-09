from django.urls import path
from . import views

from .views import SignUpView

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]