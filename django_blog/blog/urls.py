# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    # Home page (redirect to posts list)
    path('', views.PostListView.as_view(), name='home'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # CRUD URLs for blog posts
path('post/new/', views.PostCreateView.as_view(), name='post_create'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]