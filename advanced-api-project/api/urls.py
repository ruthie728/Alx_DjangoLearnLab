# api/urls.py

from django.urls import path
from . import views

# ===================== URL Patterns for API =====================
urlpatterns = [
    # ---------- Author Endpoints ----------
    path(
        'authors/', 
        views.AuthorListCreateView.as_view(), 
        name='author-list-create'
    ),
    # GET single author by ID
    path(
        'authors/<int:pk>/', 
        views.AuthorRetrieveView.as_view(), 
        name='author-detail'
    ),

    # ---------- Book Endpoints ----------
    # List all books or create a new book
    path(
        'books/', 
        views.BookListCreateView.as_view(), 
        name='book-list-create'
    ),
    # Retrieve, update, or delete a book by ID
    path(
        'books/<int:pk>/', 
        views.BookRetrieveUpdateDestroyView.as_view(), 
        name='book-detail'
    ),
]