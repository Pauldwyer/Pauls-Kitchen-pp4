from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic, View
from .forms import CustomUserCreationForm, RecipeForm, CommentForm
from .models import Recipe


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter().order_by('-published_on')
    template_name = 'recipe_list.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        # if recipe.likes.filter(id=self.request.user.id).exists():
            # liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class AddRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = form.instance.title.lower().replace(' ', '-')
        return super().form_valid(form)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
