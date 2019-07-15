from django.db import models
from django.utils import timezone
from suppliers.models import Supplier
from items.models import Item


class InvoiceHead(models.Model):
	invoice_no = models.AutoField(primary_key=True)
	invoice_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return str(self.invoice_no) + " ----- " + str(self.invoice_date.date())


class InvoiceDetail(models.Model):
	invoice_head = models.ForeignKey(InvoiceHead, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	amount = models.IntegerField()
	tax = models.IntegerField()
	
	class Meta:
		unique_together = (('invoice_head', 'item'),)
		
	def __str__(self):
		return str(self.invoice_head) + " | " + str(self.item)
