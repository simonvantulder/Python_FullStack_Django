from django.db import models

    # create a website that allows users to register books and their associated authors and give reviews
    # associate books w authors so a user can look up books by author or other books by the same author
class Book(models.Model): 
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=250,)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"< {self.title} ({self.id})>"

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    text = models.CharField(max_length=250, default="wrote a bunch of books")
    books = models.ManyToManyField("Book", related_name="authors")

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):        
        return f"< {self.first_name} {self.last_name} ({self.id})>"

