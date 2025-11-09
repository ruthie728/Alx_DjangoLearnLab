from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    login_view,
    logout_view,
)

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='list_books'),

    # Class-based view (expecting a library id)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
