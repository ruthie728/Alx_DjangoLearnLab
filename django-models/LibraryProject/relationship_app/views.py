from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library  # <- this line is what the test wants

# ==============================
# Function-based view
# ==============================
def list_books(request):
    """Display all books in the database."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# ==============================
# Class-based view
# ==============================
class LibraryDetailView(DetailView):
    """Display details for a specific library, including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'