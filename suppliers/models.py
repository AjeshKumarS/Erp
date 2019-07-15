from django.db import models
from .utils import unique_slug_generator
from django.db.models import signals


class Supplier(models.Model):
	supplier_code = models.CharField(max_length=200, primary_key=True, blank=True)
	company_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.supplier_code


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.sup_code:
		instance.sup_code = unique_slug_generator(instance)
		

signals.pre_save.connect(product_pre_save_receiver, sender=Supplier)

