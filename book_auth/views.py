from django.shortcuts import render, redirect

# from book_auth import models
from .models import Book, Author

# rendering to index webpage // passing books to index webpage
def index(request):
    context = {
        "books": Book.objects.all(),
    }
    return render(request, "index.html", context)


# creating an object then redirecting to same index page
def addBook(request):
    Book.objects.create(
        title=request.POST["title"],
        desc=request.POST["desc"],
    )
    return redirect("/")


def showBook(request, book_id):
    # print(models.getBook(book_id).authors.all())
    context = {
        "book": Book.objects.get(id=book_id),
        "authors": Author.objects.all(),
    }
    return render(request, "book_info.html", context)


def addAuthorToBook(request, book_id):
    Book.objects.get(id=book_id).authors.add(
        Author.objects.get(id=request.POST["select_author"])
    )
    return redirect(f"/books/{book_id}")


def authors(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)


# this will recieve a request.POST from html and add an instance to database
def addAuthor(request):
    Author.objects.create(
        first_name=request.POST["fname"],
        last_name=request.POST["lname"],
        notes=request.POST["notes"],
    )
    return redirect("/authors")


def showAuthor(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "books": Book.objects.all(),
    }
    return render(request, "author_info.html", context)


def addBookToAuthor(request, author_id):
    Author.objects.get(id=author_id).books.add(
        Book.objects.get(id=request.POST["select_book"])
    )

    return redirect(f"/authors/{author_id}")
