from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# List View — Read-only list of all books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet — Full CRUD (Create, Read, Update, Delete)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer