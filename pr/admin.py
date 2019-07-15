from django.contrib import admin
from .models import PRDetail, PRHead


class PRHeadAdmin(admin.ModelAdmin):
	list_display = ('pr_no', 'pr_date')
	list_display_links = ('pr_no', 'pr_date')
	search_fields = ('pr_no', 'pr_date')
	list_per_page = 30


class PRDetailAdmin(admin.ModelAdmin):
	list_display = ('pr_head', 'item', 'supplier', 'quantity', 'amount', 'tax')
	list_display_links = ('pr_head', 'item', 'supplier',)
	search_fields = ('pr_head', 'item', 'supplier',)
	list_per_page = 30
	

admin.site.register(PRHead, PRHeadAdmin)
admin.site.register(PRDetail, PRDetailAdmin)

