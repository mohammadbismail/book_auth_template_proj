from django.shortcuts import render, redirect
from book_auth import models


def renderBook(request):
    context = {
        "books": models.getBooks(),
    }

    return render(request, "index.html", context)


def renderAuthor(request):
    context = {
        "authors": models.getAuthors(),
    }
    return render(request, "authors.html", context)


def bookCascaded(request):
    pass


def authorCascaded(request):
    pass


def book(request):
    models.makeBook(request)
    return redirect("/")


def author(request):
    models.makeAuthor(request)
    return redirect("/authors")
