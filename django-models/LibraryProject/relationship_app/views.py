from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Library

# ==============================
# Function-based view (Books)
# ==============================
def list_books(request):
    """Display all books in the database."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# ==============================
# Class-based view (Library)
# ==============================
class LibraryDetailView(DetailView):
    """Display details for a specific library, including all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# ==============================
# User Authentication Views
# ==============================

# --- Register View ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --- Login View ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


# --- Logout View ---
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')