from django.db import models

class ShowManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        #all errors are strings
        if len(post_data['title']) < 2:
            errors['title'] = "TV Show title must be longer than 1 character"
        if len(post_data['network']) < 2:
            errors['network'] = "Network name must be longer than 1 character"
        if not post_data['release_date']:
            errors['release_date'] = "Must select Release Date"
        if len(post_data['description']) < 2:
            errors['description'] = "Description cannot be empty"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField(null = True)
    desc = models.CharField(max_length=250, default= "random show")
    objects = ShowManager()

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return f"< {self.title} ({self.id})>"


