from django.contrib import admin
from .models import InvoiceDetail, InvoiceHead
# Register your models here.


class InvoiceHeadAdmin(admin.ModelAdmin):
	list_display = ('invoice_no', 'invoice_date')
	list_display_links = ('invoice_no', 'invoice_date')
	search_fields = ('invoice_no', 'invoice_date')
	list_per_page = 30
	
	
class InvoiceDetailAdmin(admin.ModelAdmin):
	list_display = ('invoice_head', 'item', 'supplier', 'qty', 'amt', 'tax')
	list_display_links = ('invoice_head', 'item', 'supplier',)
	search_fields = ('invoice_head', 'item', 'supplier',)
	list_per_page = 30


admin.site.register(InvoiceHead, InvoiceHeadAdmin)
admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
