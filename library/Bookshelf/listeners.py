from django.dispatch import receiver
from  django.core.mail import send_mail
import logging
from django.conf import settings
from Bookshelf.signals import book_created , book_borrowed , book_returned

logger = logging.getLogger(__name__)

@receiver(book_created)
def handle_book_created(sender ,instance , created_at , **kwargs):
    logger.info(f'A new book is created named {instance} at {created_at}')
    print(f'A new book is created named {instance} at {created_at}')


@receiver(book_borrowed)
def handle_update_borrowed(sender , instance,user , **kwargs):
    # instance.user_borrowed = True
    # instance.save()
    print(f"Book {instance.title} was borrowed by {user.username}")

@receiver(book_returned)
def handle_book_returned(sender , instance , user , **kwargs):
    # instance.user_borrowed = False
    # instance.save()
    print(f"Book {instance.title} was returned")
    # logger.info(f"Book {instance.title} was returned by {user.username}")



# @receiver(book_borrowed)
# def send_borrowed_email(sender, instance, user, **kwargs):
#     subject = f"Book Borrowed: {instance.title}"
#     message = f"Dear {user.first_name},\n\nYou have successfully borrowed the book '{instance.title}'."
#     from_email = settings.DEFAULT_FROM_EMAIL
#     recipient_list = [user.user_email]
#     send_mail(subject, message, from_email, recipient_list)