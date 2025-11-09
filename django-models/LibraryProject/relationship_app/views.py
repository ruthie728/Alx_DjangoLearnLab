from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Library, UserProfile

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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# ==============================
# Role-Based Access Views
# ==============================

# Helper functions to check roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Admin View ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# --- Librarian View ---
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# --- Member View ---
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')