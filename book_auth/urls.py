from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("addBook/", views.addBook),
    path("books/<int:book_id>", views.showBook),
    path("books/add_author_to_book/<int:book_id>", views.addAuthorToBook),
    path("authors/", views.authors),
    path("authors/addAuthor/", views.addAuthor),
    path("authors/<int:author_id>", views.showAuthor),
    path("authors/add_book_to_author/<int:author_id>", views.addBookToAuthor),
]
