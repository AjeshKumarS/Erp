from django.db import models
from django.utils import timezone
from suppliers.models import Supplier
from items.models import Item 

class POHead(models.Model):
    po_no = models.IntegerField(primary_key=True)
    po_date = models.DateTimeField(default = timezone.now)
    appr_date = models.DateTimeField(default = timezone.now)



class PODetail(models.Model):
	tax = models.IntegerField()
	amt = models.IntegerField()
	qty = models.IntegerField()
	po_head = models.ForeignKey(POHead, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	
	class Meta:
	    unique_together = (('po_head', 'item'),)

