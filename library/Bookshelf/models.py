from django.db import models
from .signals import book_created , book_borrowed , book_returned
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class User(models.Model):
    username = models.CharField(max_length=20 , db_index = True)
    user_email = models.EmailField(db_index= True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        indexes = [
            models.Index(fields=['username']),  
            models.Index(fields=['user_email']),  
        ]
    
class Book(models.Model):
    title = models.CharField(max_length=50 , db_index=True)
    isbn = models.CharField(max_length=13 , unique = True , db_index=True)
    published_date = models.DateField()
    author = models.ForeignKey('Author' , on_delete=models.CASCADE , related_name='books' )
    user_borrowed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING , blank = True , null= True , related_name='books')

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields = ['title']),
            models.Index(fields = ['isbn']),
        ]

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(Book, self).save(*args, **kwargs)

        if created:
            book_created.send(sender=self.__class__, instance=self, created_at=timezone.now())

        if not created:
            if self.user_borrowed or self.user != None:
                    book_borrowed.send(sender=self.__class__, instance=self, user=self.user)
            else:
                    book_returned.send(sender=self.__class__, instance=self, user=self.user)