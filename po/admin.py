from django.contrib import admin
from .models import PODetail, POHead


class POHeadAdmin(admin.ModelAdmin):
	list_display = ('po_no', 'po_date')
	list_display_links = ('po_no', 'po_date')
	search_fields = ('po_no', 'po_date')
	list_per_page = 30


class PODetailAdmin(admin.ModelAdmin):
	list_display = ('po_head', 'item', 'supplier', 'quantity', 'amount', 'tax')
	list_display_links = ('po_head', 'item', 'supplier',)
	search_fields = ('po_head', 'item', 'supplier',)
	list_per_page = 30
	

admin.site.register(POHead, POHeadAdmin)
admin.site.register(PODetail, PODetailAdmin)

