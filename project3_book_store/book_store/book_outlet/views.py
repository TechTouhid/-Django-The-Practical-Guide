from django.db.models import Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book


# Create your views here.
def index(request):
    # we can sort the data using order_by() function | add - for descending order
    # books = Book.objects.all()
    books = Book.objects.all().order_by("-id")
    #  aggregation functions
    total_number_of_book = books.count()
    average_rating = books.aggregate(Avg("rating"))  # here rating is taken form model
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_book": total_number_of_book,
        "average_rating": average_rating
    })


def book_details(request, slug):
    #  Method 1
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    #  Method 2
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_details.html/", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })
