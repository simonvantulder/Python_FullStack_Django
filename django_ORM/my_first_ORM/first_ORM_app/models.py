from django.db import models

class User(models.Model):
    #id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age=models.IntegerField()
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"<User object: {self.title} ({self.id})>"
    def __repr__(self):
        return "Title: {}" .format(self.title) #returns title as variable