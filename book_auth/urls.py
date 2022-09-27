from django.urls import path
from . import views

urlpatterns = [
    path("", views.renderBook),
    path("addBook/", views.book),
    path("authors/", views.renderAuthor),
    path("authors/addAuthor/", views.author),
    # path("books/<int:my_val>", views.bookCascaded),
    # path("authors/<int:my_val>",views.authorCascaded),
]
