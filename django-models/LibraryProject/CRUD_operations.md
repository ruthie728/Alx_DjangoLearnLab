# CRUD Operations for Book Model

## Create Book
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Check the created book
book
```
```output
<Book: 1984 by George Orwell (1949)>
```

## Retrieve Book
```python
# Retrieve all books
Book.objects.all()
```
```output
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
```

## Update Book
```python
# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Check updated book
book
```
```output
<Book: Nineteen Eighty-Four by George Orwell (1949)>
```

## Delete Book
```python
# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()
```
```output-expected
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
```