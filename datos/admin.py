from django.contrib import admin

from .models import TemplateData, TemplateDataLog, TemplateDataUploadLog

@admin.register(TemplateData)
class TemplateDataAdmin(admin.ModelAdmin):
	list_display = ('id', 'leasid', 'bldgid', 'suitid', 'occpname', 'fields')
	ordering = ('bldgid',)
	search_fields = ('bldgid',)
	list_filter = ('bldgid',)

@admin.register(TemplateDataLog)
class TemplateDataLogAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'bldgid', 'created', 'first_validation', 'second_validation')
	ordering = ('created',)

@admin.register(TemplateDataUploadLog)
class TemplateDataUploadLogAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'bldgid', 'active')
	ordering = ('active',)