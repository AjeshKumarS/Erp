from django.contrib import admin
from .models import Item, Uom


class ItemAdmin(admin.ModelAdmin):
	list_display = ('item_code', 'item_desc', 'price', 'uom')
	list_display_links = ('item_code', 'item_desc')
	search_fields = ('item_code', 'item_desc')
	list_per_page = 30


class UomAdmin(admin.ModelAdmin):
	list_display = ('id', 'uom')
	list_display_links = ('id', 'uom')
	search_fields = ('id', 'uom')
	list_per_page = 30
	

admin.site.register(Item, ItemAdmin)
admin.site.register(Uom, UomAdmin)
