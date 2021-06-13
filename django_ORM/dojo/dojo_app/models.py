from django.db import models

class Dojo(models.Model): # create a dojo school with location and description
    name = models.CharField(max_length=100)     
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    desc = models.CharField(max_length=250, default= "old dojo")
    
    created_at=models.DateTimeField(auto_now_add=True) # keep track of instance creation and update
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        #statement return dojo name and id in the terminal/shell when printed out
        return f"< {self.name} ({self.id})>"



class Ninja(models.Model): # ceate a ninja associate with one of the dojos 
    
    # model w foreign key must be below its associated model
    dojo_ID = models.ForeignKey('Dojo', related_name= "ninjas", null= True, on_delete = models.CASCADE) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):        
        return f"< {self.first_name} ({self.id})>"

