from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


# 5 UserProfile model for Role-Based Access
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Signal to automatically create or update a UserProfile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()