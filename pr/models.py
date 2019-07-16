from django.db import models
from django.utils import timezone
from suppliers.models import Supplier
from items.models import Item


class PRHead(models.Model):
	pr_no = models.AutoField(primary_key=True)
	pr_date = models.DateTimeField(default=timezone.now)
	approved_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return str(self.pr_no) + " ----- " + str(self.pr_date.date())


class PRDetail(models.Model):
	pr_head = models.ForeignKey(PRHead, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	amount = models.IntegerField()
	tax = models.IntegerField()
	
	class Meta:
		unique_together = (('pr_head', 'item'),)
		
	def __str__(self):
		return str(self.pr_head) + " | " + str(self.item)
