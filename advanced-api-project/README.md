# Advanced API Project - Django REST Framework

## Overview
This project demonstrates custom and generic views using Django REST Framework for managing Authors and Books.  
It includes CRUD operations, permission controls, customized behaviors, and advanced filtering/searching/ordering functionality.

## API Endpoints

### Authors
| Endpoint               | Method | Permissions          | Action                  |
|------------------------|--------|-------------------|------------------------|
| /api/authors/          | GET    | Anyone             | List all authors       |
| /api/authors/          | POST   | Authenticated only | Create a new author    |
| /api/authors/<id>/     | GET    | Anyone             | Retrieve a single author |

### Books
| Endpoint               | Method | Permissions          | Action                  |
|------------------------|--------|-------------------|------------------------|
| /api/books/            | GET    | Anyone             | List all books         |
| /api/books/            | POST   | Authenticated only | Create a new book      |
| /api/books/<id>/       | GET    | Anyone             | Retrieve a single book |
| /api/books/<id>/       | PUT/PATCH | Authenticated only | Update a book       |
| /api/books/<id>/       | DELETE | Authenticated only | Delete a book          |

## Customizations
- `BookListCreateView.perform_create()` handles custom logic during book creation.
- `BookRetrieveUpdateDestroyView.perform_update()` allows adding extra logic during updates.
- Filtering, searching, and ordering are implemented in the `BookListCreateView` using DRF’s `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter`.

## Permissions
- Authenticated users can create, update, or delete authors and books.
- Unauthenticated users have read-only access.

## Testing
The API is thoroughly tested using Django REST Framework’s `APITestCase`.  

### Testing Strategy

1. **Test Setup**
   - `setUp()` method creates a test user, an author, and some book instances before each test.
   - `APIClient` simulates API requests in an isolated environment.

2. **Books CRUD Tests**
   - **List Books:** Ensure all books are returned with status `200 OK`.
   - **Retrieve Book:** Validate retrieval of a single book by ID.
   - **Create Book:** Authenticated users can create books (`201 CREATED`); unauthenticated requests are blocked (`403 FORBIDDEN`).
   - **Update Book:** Updates persist correctly.
   - **Delete Book:** Book is removed and count is updated.

3. **Filtering, Searching, and Ordering**
   - **Filtering:** Test filtering by `publication_year`.
   - **Searching:** Test search by `title`.
   - **Ordering:** Test ordering by `publication_year`.

4. **Authors CRUD Tests**
   - **List Authors:** Ensure all authors are returned with `200 OK`.
   - **Retrieve Author:** Validate retrieval of a single author by ID.
   - **Create Author:** Authenticated users can create authors; unauthenticated requests are blocked.

5. **Permissions and Authentication**
   - Authenticated users can create, update, delete.
   - Unauthenticated users have read-only access.
   - Protected endpoints reject unauthorized requests.

### Running the Tests

Execute all tests in the `api` app:

```bash
python manage.py test api