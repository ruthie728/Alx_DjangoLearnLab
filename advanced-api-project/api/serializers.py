# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
import datetime

# Purpose:
#   Define serializers for Book and Author.
#   - BookSerializer: serializes all Book fields and enforces validation
#     to ensure publication_year is not in the future.
#   - AuthorSerializer: serializes Author fields and includes nested books via BookSerializer.
#
# Relationship handling:
#   The AuthorSerializer includes a nested 'books' field (many=True, read_only=True),
#   which uses BookSerializer to represent related Book objects. This allows an API
#   response for an author to include the list of their books.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # serialize all Book model fields
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Field-level validation to ensure publication_year is not in the future.
        Raises a serializers.ValidationError if the year > current year.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    A compact BookSerializer used when nested inside AuthorSerializer.
    Read-only by default in this example.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

class AuthorSerializer(serializers.ModelSerializer):
    # books: nested list of books related to this author.
    # using NestedBookSerializer to avoid recursion and reduce payload.
    books = NestedBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']