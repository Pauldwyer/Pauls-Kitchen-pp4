from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic, View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, RecipeForm, CommentForm
from .models import Recipe, CustomUser


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


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
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = recipe
            comment.save()
            messages.success(request, 'Your comment has been added successfully. It just needs to be authorised')
        else:
            messages.error(request, 'There was an error adding your comment. Please try again.')
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
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


class EditRecipeView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
