# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    # Home page
    path('', views.PostListView.as_view(), name='home'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # Post CRUD
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs (checker requires pk)
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # -------------------------
    # TAGGING + SEARCH (NEW)
    # -------------------------

    # List all posts for a specific tag
    path('tags/<str:tag_name>/', views.PostsByTagView.as_view(), name='posts_by_tag'),

    # Search URL
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]