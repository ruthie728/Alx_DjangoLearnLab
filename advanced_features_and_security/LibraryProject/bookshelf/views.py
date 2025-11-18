from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm  # import the form
from .forms import ExampleForm
# ------------------------------
# View all books
# Secure: Uses ORM to fetch data, permission required
# ------------------------------
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Safe ORM query, no raw SQL
    return render(request, "bookshelf/book_list.html", {"books": books})

# ------------------------------
# Create a new book using BookForm
# Secure: Validates user input, checks permission, CSRF protection via template
# ------------------------------
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # validates automatically
            form.save()  # safe creation
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/create_book.html", {"form": form})

# ------------------------------
# Edit an existing book using BookForm
# Secure: Uses get_object_or_404 to avoid exposing database errors
# ------------------------------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Safe retrieval
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # safe update
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/edit_book.html", {"form": form, "book": book})

# ------------------------------
# Delete a book
# Secure: Uses permission check, safe deletion
# ------------------------------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/delete_book.html", {"book": book})
