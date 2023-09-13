from django.contrib import admin
from .models import Book, BookTitle

# Register your models here.
admin.site.register(BookTitle)
admin.site.register(Book)