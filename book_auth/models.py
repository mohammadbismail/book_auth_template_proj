from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(null=True)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Book, related_name="authors")

#desc: return all objects instances from class Book
#input: NA
#output: all objects from class Book
def getBooks():
    return Book.objects.all()

#desc: return all objects instances from class Author
#input: NA
#output: all objects from class Author
def getAuthors():
    return Author.objects.all()

#desc: making an author object out of coming request POST
#input:post request from html coming to server side
#output: an object of specific class (Book)
def makeBook(request):
    Book.objects.create(
        title=request.POST["title"],
        desc=request.POST["desc"],
    )

#desc: making an author object out of coming request POST
#input:post request from html coming to server side
#output: an object of specific class (Author)
def makeAuthor(request):
    Author.objects.create(
        first_name=request.POST["fname"],
        last_name=request.POST["lname"],
        notes=request.POST["notes"],
    )

#desc: given an id of book&author this function is supposed to return a relation of both
#input: id instances of both classes book&author
#output: a realtion between both instances 
def makeRelation(book_id, author_id):
    Book.objects.get(id=book_id).authors.add(Author.objects.get(id=author_id))
