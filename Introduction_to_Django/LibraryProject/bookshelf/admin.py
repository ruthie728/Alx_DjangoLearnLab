from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show columns in list view
    search_fields = ('title', 'author')                     # allow search
    list_filter = ('publication_year',)                     # add filter sidebar

admin.site.register(Book, BookAdmin)