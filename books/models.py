from django.db import models

# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=20)
    book_pages = models.IntegerField()
    book_author = models.CharField(max_length=20)
    book_description = models.TextField()


