# api/views.py

from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# ===================== Author Views =====================

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    GET: List all authors
    POST: Create a new author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Auth required for POST

    def perform_create(self, serializer):
        """
        Customize creation behavior for authors if needed.
        Example: automatically set a field or log creation.
        """
        serializer.save()  # Add extra fields here if your Author model has them


class AuthorRetrieveView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single author by ID
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view author details


# ===================== Book Views =====================

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Auth required for POST

    def perform_create(self, serializer):
        """
        Customize creation behavior for books.
        Example: associate the current logged-in user as the creator.
        """
        # If your Book model has a 'created_by' field:
        # serializer.save(created_by=self.request.user)
        serializer.save()  # Default save without extra fields


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book by ID
    PUT/PATCH: Update a book
    DELETE: Remove a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Auth required for update/delete

    def perform_update(self, serializer):
        """
        Customize update behavior for books.
        Example: track the user who updated the book or perform extra validation.
        """
        # If your Book model has a 'last_updated_by' field:
        # serializer.save(last_updated_by=self.request.user)
        serializer.save()  # Default update