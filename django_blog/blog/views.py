# blog/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post
from .forms import PostForm


# ---------------------------
# Blog Post CRUD Views
# ---------------------------

# Mixin to ensure only authors can edit or delete posts
class AuthorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/login/'  # Change to your login page if needed

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


# List all posts (public)
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']  # newest first


# View a single post (public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# Create a new post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update a post (only author can update)
class PostUpdateView(AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


# Delete a post (only author can delete)
class PostDeleteView(AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')  # fixed URL name


# ---------------------------
# User Profile View
# ---------------------------
@login_required
def profile_view(request):
    """
    Display and edit the current user's profile.
    """
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("blog:profile")  # Ensure this matches your urls.py

    return render(request, "blog/profile.html")