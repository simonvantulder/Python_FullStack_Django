from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=250, default= "old dojo")
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):        
        return f"< {self.name} ({self.id})>"



class Ninja(models.Model):
    dojo_ID = models.ForeignKey('Dojo', related_name= "ninjas", null= True, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)




    def __str__(self):        
        return f"< {self.first_name} ({self.id})>"

