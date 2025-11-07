from django.db import models

# 1 Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2 Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # ForeignKey: Each book has one author, one author can have many books

    def __str__(self):
        return self.title

# 3 Library model
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    # ManyToMany: A library can have many books, a book can be in many libraries

    def __str__(self):
        return self.name

# 4 Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    # OneToOne: Each library has one librarian, one librarian belongs to one library

    def __str__(self):
        return self.name