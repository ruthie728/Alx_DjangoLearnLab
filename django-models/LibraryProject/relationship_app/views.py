from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# ==============================
# Function-based view
# ==============================
def list_books(request):
    """Display all books in the database."""
    books = Book.objects.all()
    context = {'books': books}
    # Correct template path expected by the test
    return render(request, 'relationship_app/list_books.html', context)


# ==============================
# Class-based view
# ==============================
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # correct path
    context_object_name = 'library'  # template will use {{ library }}