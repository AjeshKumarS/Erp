from django.db import models
from django.utils import timezone


class Supplier(models.Model):
	comp_name = models.CharField(max_length=50)
	f_name = models.CharField(max_length=100)
	l_name = models.CharField(max_length=100)
	sup_code = models.CharField(max_length=10,primary_key=True)

