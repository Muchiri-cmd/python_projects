from django.db import models

# Create your models here.
class Pizza(models.Model):
    #holds names and values such as Hawaiian and meat lovers
    name=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        #returns string name of model
        return self.text

class Topping(models.Model):
    #holds name and toppings
    name=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='toppings'
    
    def __str__(self):
        #returns toppings name 
        return self.topping
                              
