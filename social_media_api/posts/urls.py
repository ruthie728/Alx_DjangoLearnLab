from django.urls import path
from .views import (
    feed_view,
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    LikePostView,
    UnlikePostView,
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),

    # Feed
    path('feed/', feed_view, name='post-feed'),

    # Likes
    path('<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
]
