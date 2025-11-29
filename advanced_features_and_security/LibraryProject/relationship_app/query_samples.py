# relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author) # thanks to related_name='books' in Book model
        return books
    except Author.DoesNotExist:
        return []

# 2️⃣ List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # thanks to ManyToManyField
    except Library.DoesNotExist:
        return []

# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library) # thanks to OneToOneField related_name
    except Library.DoesNotExist:
        return None