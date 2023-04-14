from django.contrib import admin
from .models import ToMri

# Register your models here.

@admin.register(ToMri)
class ToMriAdmin(admin.ModelAdmin):
	list_display = ('BLDGID', 'LEASID', 'DESCRPTN', 'VALUE')
	ordering = ('BLDGID',)
	search_fields = ('BLDGID', 'LEASID', 'DESCRPTN')