from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post, Comment
from .forms import PostForm, CommentForm


# ---------------------------
# Blog Post CRUD Views
# ---------------------------

class AuthorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/login/'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        # Tags are handled automatically by TaggableManager
        return response

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # Tags are updated automatically by TaggableManager
        return response

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:posts_list')


# ---------------------------
# Comment CRUD Views
# ---------------------------

class CommentAuthorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/login/'

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(CommentAuthorRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(CommentAuthorRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.post.pk})


# ---------------------------
# User Profile View
# ---------------------------
@login_required
def profile_view(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("blog:profile")

    return render(request, "blog/profile.html")