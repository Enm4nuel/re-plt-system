from django.contrib import admin
from .models import ToMri

# Register your models here.

@admin.register(ToMri)
class ToMriAdmin(admin.ModelAdmin):
	list_display = ('bldgid', 'leasid', 'descrptn', 'tranamt')
	