from django.db import models
from django.db import models
from django.utils import timezone
from suppliers.models import Supplier
from items.models import Item 

class PRHead(models.Model):
    pr_no = models.IntegerField(primary_key=True)
    pr_date = models.DateTimeField(default = timezone.now)
    appr_date =models.DateTimeField(default = timezone.now)
    
class PRDetail(models.Model):
    tax = models.IntegerField()
    amt = models.IntegerField()
    qty = models.IntegerField()
    pr_head = models.ForeignKey(PRHead, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    class Meta:
    	unique_together = (('pr_head', 'item'),)

