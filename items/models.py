from django.db import models
from django.utils import timezone


class Uom(models.Model):
    uom = models.CharField(max_length = 50 ,unique = True) 
    
    def __str__(self):
        return self.uom


class Item(models.Model):
    item_code = models.IntegerField(primary_key = True)
    item_desc = models.CharField(max_length = 300)
    price = models.IntegerField()
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE)
   
    
    
    def __str__(self):
        return self.item_desc








    




    
    

