from django.contrib import admin
from .models import Supplier


class SupplierAdmin(admin.ModelAdmin):
	list_display = ('supplier_code', 'company_name', 'first_name', 'last_name')
	list_display_links = ('supplier_code', 'company_name', 'first_name', 'last_name')
	search_fields = ('supplier_code', 'company_name', 'first_name', 'last_name')
	list_per_page = 30
	

admin.site.register(Supplier, SupplierAdmin)


