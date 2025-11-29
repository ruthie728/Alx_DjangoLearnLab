# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        """
        Runs before every test. Sets up users, authors, and books.
        """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')

        # Create a test author
        self.author = Author.objects.create(name='Test Author')

        # Create test books
        self.book1 = Book.objects.create(title='Book One', author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author=self.author, publication_year=2021)

        # API client
        self.client = APIClient()

    # --------------------- BOOKS TESTS ---------------------

    def test_list_books(self):
        url = reverse('books-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse('books-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('books-create')
        data = {'title': 'Book Three', 'author': self.author.id, 'publication_year': 2022}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('books-create')
        data = {'title': 'Book Three', 'author': self.author.id, 'publication_year': 2022}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('books-update', args=[self.book1.id])
        data = {'title': 'Book One Updated', 'author': self.author.id, 'publication_year': 2020}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Book One Updated')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('books-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --------------------- FILTER, SEARCH, ORDER TESTS ---------------------

    def test_filter_books_by_publication_year(self):
        url = reverse('books-list') + '?publication_year=2020'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books_by_title(self):
        url = reverse('books-list') + '?search=Book Two'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')

    def test_order_books_by_publication_year(self):
        url = reverse('books-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)

    # --------------------- AUTHORS TESTS ---------------------

    def test_list_authors(self):
        url = reverse('author-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_author(self):
        url = reverse('author-detail', args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.author.name)

    def test_create_author_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('author-list-create')
        data = {'name': 'New Author'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 2)

    def test_create_author_unauthenticated(self):
        url = reverse('author-list-create')
        data = {'name': 'New Author'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)