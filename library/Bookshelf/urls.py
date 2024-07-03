from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Bookshelf_home'),
    path('books/', views.books, name='books'),
    path('books/year/<int:published_year>/', views.books_by_year, name='books_by_year'),
    path('books/author/<int:author_id>/', views.books_by_author, name='books_by_author'),
    path('books/user/<int:user_id>/', views.books_with_user, name='books_with_user'),
]