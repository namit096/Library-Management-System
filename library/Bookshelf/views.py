from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Book , User , Author

def home(request):
    return HttpResponse("This is BookShelf Home Page")

def books(request):
    books = Book.objects.all()
    response_text = ""
    for book in books:
        response_text += f"Title: {book.title}\n"
        response_text += f"ISBN: {book.isbn}\n"
        response_text += f"Published Date: {book.published_date}\n"
        response_text += f"Author: {book.author.first_name} {book.author.last_name}\n"
        response_text += f"User Borrowed: {book.user_borrowed}\n"
        if book.user:
            response_text += f"Borrowed By: {book.user.first_name} {book.user.last_name}\n"
        response_text += f"Created At: {book.created_at}\n"
        response_text += f"Updated At: {book.updated_at}\n"
        response_text += "\n"  # Add a blank line between books
    return HttpResponse(response_text , content_type="text/plain")

def books_by_year(request , published_year):
    books = Book.objects.filter(published_date__year=published_year)
    response_text = ""
    for book in books:
        response_text += f"Title: {book.title}\n"
        response_text += f"ISBN: {book.isbn}\n"
        response_text += f"Published Date: {book.published_date}\n"
        response_text += f"Author: {book.author.first_name} {book.author.last_name}\n"
        response_text += f"User Borrowed: {book.user_borrowed}\n"
        if book.user:
            response_text += f"Borrowed By: {book.user.first_name} {book.user.last_name}\n"
        response_text += f"Created At: {book.created_at}\n"
        response_text += f"Updated At: {book.updated_at}\n"
        response_text += "\n"  # Add a blank line between books
    return HttpResponse(response_text , content_type="text/plain")

def books_by_author(request , author_id):
    books = Book.objects.filter(author__id=author_id)
    response_text = ""
    for book in books:
        response_text += f"Title: {book.title}\n"
        response_text += f"ISBN: {book.isbn}\n"
        response_text += f"Published Date: {book.published_date}\n"
        response_text += f"Author: {book.author.first_name} {book.author.last_name}\n"
        response_text += f"User Borrowed: {book.user_borrowed}\n"
        if book.user:
            response_text += f"Borrowed By: {book.user.first_name} {book.user.last_name}\n"
        response_text += f"Created At: {book.created_at}\n"
        response_text += f"Updated At: {book.updated_at}\n"
        response_text += "\n"  # Add a blank line between books
    return HttpResponse(response_text , content_type="text/plain")

def books_with_user(request , user_id):
    books = Book.objects.filter(user_id=user_id)
    response_text = ""
    for book in books:
        response_text += f"Title: {book.title}\n"
        response_text += f"ISBN: {book.isbn}\n"
        response_text += f"Published Date: {book.published_date}\n"
        response_text += f"Author: {book.author.first_name} {book.author.last_name}\n"
        response_text += f"User Borrowed: {book.user_borrowed}\n"
        if book.user:
            response_text += f"Borrowed By: {book.user.first_name} {book.user.last_name}\n"
        response_text += f"Created At: {book.created_at}\n"
        response_text += f"Updated At: {book.updated_at}\n"
        response_text += "\n"  # Add a blank line between books
    return HttpResponse(response_text , content_type="text/plain")

