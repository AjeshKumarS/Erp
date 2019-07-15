from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
	list_display = ('sup_code', 'comp_name', 'f_name', 'l_name')
	list_display_links = ('sup_code', 'comp_name', 'f_name', 'l_name')
	search_fields = ('sup_code', 'comp_name', 'f_name', 'l_name')
	list_per_page = 30
	

admin.site.register(Supplier, SupplierAdmin)


