# api/models.py

from django.db import models

# Purpose:
#   Define Author and Book models.
#   Author has a one-to-many relationship to Book (one Author -> many Books).
#
# Fields:
#   Author:
#     - name: stores the author's name (string)
#   Book:
#     - title: the book title (string)
#     - publication_year: the year the book was published (integer)
#     - author: ForeignKey to Author establishing the one-to-many relationship

class Author(models.Model):
    # name of the author
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    # title of the book
    title = models.CharField(max_length=255)

    # publication_year stores the year the book was published; integer field
    publication_year = models.IntegerField()

    # author is a ForeignKey to Author, establishing one-to-many relation:
    # - related_name='books' allows accessing author.books.all()
    # - on_delete=models.CASCADE means deleting an Author will also delete their Books.
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"