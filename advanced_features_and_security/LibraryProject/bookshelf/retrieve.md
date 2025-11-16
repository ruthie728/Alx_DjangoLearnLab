# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the book you created
book = Book.objects.get(title="1984")

# Display the book details
book
```

```Output
<Book: 1984 by George Orwell (1949)>
```