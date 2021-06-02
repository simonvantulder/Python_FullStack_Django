from django.db import models
from datetime import datetime
import bcrypt 
import re # import regex for email validation

class UserManager(models.Manager):
    def login_validator(self, post_data):
        errors = {}

        user_list = User.objects.filter(email = post_data['email'])
        if len(user_list) > 0:
            user = user_list[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors['password'] = "INVALID CREDENTIALS"
        else:
                errors['email'] = "INVALID CREDENTIALS"
        return errors


    def validator(self, post_data):
        DAYS_FOR_13_YRS=4749
        errors = {}

        #all errors are strings
        if len(post_data['name']) < 2:
            errors['name'] = "Name must be longer than 1 character"
        if len(post_data['alias']) < 2:
            errors['alias'] = "Alias name must be longer than 1 character"

        if len(post_data['birthday']) < 2:
            errors['birthday'] = "Must enter a birthday."
        else:
            post_date = datetime.strptime(post_data['birthday'], "%Y-%m-%d")
            curr_date = datetime.today()
            age = curr_date - post_date
            if curr_date < post_date:
                errors['birthday'] = "birthday must be in the past"
            elif (age.days < DAYS_FOR_13_YRS):
                errors['birthday'] = "You must be 13yrs old to register"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid Email address!"
        else:
                user_list = User.objects.filter(email = post_data['email'])
                if len(user_list) > 0:
                    errors['email'] = 'Email is being used by another user.'
        if len(post_data['password']) < 3:
            errors['password'] = "Passwords must be at least 4 characters long."
        elif post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "Password and Confirm Password must match."

        return errors

class User(models.Model):

    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthday = models.DateTimeField(null = True)
    password = models.CharField(max_length=100)
    objects = UserManager()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return f"< {self.name} ({self.id})>"


class Book(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    #REVIEWs = 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"< {self.title} ({self.id})>"


class Author(models.Model):
    name = models.CharField(max_length=100)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return f"< {self.name} ({self.id})>"


class Review(models.Model):
    book = models.ForeignKey("Book", related_name = "reviews", on_delete = models.CASCADE)
    likes = models.ManyToManyField("User", related_name = "likes")
    users = models.ForeignKey("User", related_name = "reviews", on_delete = models.CASCADE)

    content = models.CharField(max_length=100)
    rating = models.IntegerField()
    objects = UserManager()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return f"< {self.book} ({self.id})>"

