from django.dispatch import Signal, receiver

book_created = Signal()

book_borrowed = Signal()

book_returned = Signal()

