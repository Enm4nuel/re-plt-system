from django.contrib import admin
from .models import Template, TemplateLog, TemplateMonthlyCfg, TemplateMonthlyCfgLog

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

@admin.register(TemplateMonthlyCfg)
class TemplateMonthlyCfgAdmin(admin.ModelAdmin):
	list_display = ('id', 'rate', 'date')
	ordering = ('-date',)

@admin.register(TemplateMonthlyCfgLog)
class TemplateMonthlyCfgLogAdmin(admin.ModelAdmin):
	list_display = ('id', 'rate', 'created')
	ordering = ('created',)
	readonly_fields = ('id', 'rate', 'created')
