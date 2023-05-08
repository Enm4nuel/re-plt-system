from django.contrib import admin
from .models import Template, TemplateLog

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
	list_display = ('id', 'bldgid', 'currcode', 'fields')
	ordering = ('bldgid',)
	search_fields = ('bldgid',)

@admin.register(TemplateLog)
class TemplateLogAdmin(admin.ModelAdmin):
	list_display = ('bldgid', 'batch', 'invoice_date', 'created')
	ordering = ('invoice_date',)
	search_fields = ('batch', 'bldgid',)
	readonly_fields = ('bldgid', 'batch', 'invoice_date', 'created')
