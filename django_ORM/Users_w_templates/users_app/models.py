from django.db import models

class Users(models.Model): # convention is to name the class with a capital letter and singular form so User not Users...whoops, change for next time
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=255)
    age=models.IntegerField()



    def __str__(self):
        return f"< {self.first_name} ({self.id})>"
