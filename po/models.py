from django.db import models
from django.utils import timezone
from suppliers.models import Supplier
from items.models import Item


class POHead(models.Model):
	po_no = models.AutoField(primary_key=True)
	po_date = models.DateTimeField(default=timezone.now)
	approved_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return str(self.po_no) + " ----- " + str(self.po_date.date())


class PODetail(models.Model):
	po_head = models.ForeignKey(POHead, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	amount = models.IntegerField()
	tax = models.IntegerField()
	
	class Meta:
		unique_together = (('po_head', 'item'),)
		
	def __str__(self):
		return str(self.po_head) + " | " + str(self.item)
