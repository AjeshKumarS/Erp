from django.db import models
from django.utils import timezone
from suppliers.models import Supplier
from items.models import Item 


class InvoiceHead(models.Model):
    invoice_no = models.IntegerField(primary_key=True)
    invoice_date = models.DateTimeField(default = timezone.now)
	


class InvoiceDetail(models.Model):
	tax = models.IntegerField()
	amt = models.IntegerField()
	qty = models.IntegerField()
	invoice_head = models.ForeignKey(InvoiceHead, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	
	class Meta:
	    unique_together = (('invoice_head', 'item'),)

    
     


    
    
    
    
