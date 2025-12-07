# blog/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# List all posts — public
class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'   # template we will create
    context_object_name = 'posts'
    paginate_by = 10  # optional pagination

# View a single post — public
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create a new post — authenticated users only
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = '/admin/login/'  # default login page; adjust if you add custom auth

    def form_valid(self, form):
        # set the post author to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post — only author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = '/admin/login/'

    def test_func(self):
        # only author can edit
        post = self.get_object()
        return post.author == self.request.user

# Delete a post — only author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')
    login_url = '/admin/login/'

    def test_func(self):
        # only author can delete
        post = self.get_object()
        return post.author == self.request.user
    
    # --- User Profile View ---
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def profile_view(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()  # important for the checker

        return redirect("blog:profile")

    return render(request, "blog/profile.html")