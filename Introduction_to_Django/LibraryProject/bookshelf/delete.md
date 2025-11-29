# Delete Book

```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try to retrieve all books to confirm deletion
Book.objects.all()
```

```output-expected
<QuerySet [<Book: 1984 by George Orwell (1949)>]>
```