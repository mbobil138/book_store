from django.shortcuts import render
from django.http import Http404
from . models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))  # rating__avg, if min: rating__min in html

    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating":avg_rating,
    })

def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "best_selling": book.is_bestselling,
        "author": book.author,
        "rating": book.rating
    })