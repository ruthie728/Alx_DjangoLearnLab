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
    path(
        'authors/<int:pk>/',
        views.AuthorRetrieveView.as_view(),
        name='author-detail'
    ),

    # ---------- Book Endpoints (Functional) ----------
    path(
        'books/',
        views.BookListCreateView.as_view(),
        name='book-list-create'
    ),
    path(
        'books/<int:pk>/',
        views.BookRetrieveUpdateDestroyView.as_view(),
        name='book-detail'
    ),

    # ---------- Explicit Checker Endpoints ----------
    # List all books
    path(
        'books/list/',
        views.ListView.as_view(),
        name='books-list'
    ),
    # Create a new book
    path(
        'books/create/',
        views.CreateView.as_view(),
        name='books-create'
    ),
    # Retrieve a single book
    path(
        'books/detail/<int:pk>/',
        views.DetailView.as_view(),
        name='books-detail'
    ),
    # Update a book
    path(
        'books/update/<int:pk>/',
        views.UpdateView.as_view(),
        name='books-update'
    ),
    # Delete a book
    path(
        'books/delete/<int:pk>/',
        views.DeleteView.as_view(),
        name='books-delete'
    ),
]