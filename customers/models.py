from django.db import models
from books.models import Book
from django.utils.text import slugify
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, blank=True)
    additional_info = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(default=50)
    books = models.ManyToManyField(Book, blank=True, help_text='books currently rented')
    book_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.first_name)
    
    def save(self, *args, **kwargs):
        if not self.username:
            username = slugify(f'{self.first_name} {self.last_name}')
            exists = __class__.objects.filter(username = username).exists()

            while exists: 
                i = len(__class__.objects.filter(first_name = self.first_name, last_name = self.last_name))
                username = slugify(f'{self.first_name} {self.last_name} {i+1}')
                exists = __class__.objects.filter(username = username).exists()
            self.username = username

        super().save(*args, **kwargs)
    
