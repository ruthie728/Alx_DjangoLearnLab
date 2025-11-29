# Advanced API Project - Django REST Framework

## Overview
This project demonstrates custom and generic views using Django REST Framework for managing Authors and Books.  
It includes CRUD operations, permission controls, and customized behaviors.

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

## Permissions
- Authenticated users can create, update, or delete authors and books.
- Unauthenticated users have read-only access.

## Testing
- Use Django REST Framework’s browsable API for manual testing.
- Log in to test protected endpoints for creation, updating, and deletion.