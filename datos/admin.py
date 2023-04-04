from django.contrib import admin

from .models import Datosp, LogDatosP

@admin.register(Datosp)
class DatosAdmin(admin.ModelAdmin):
	list_display = ('id', 'leasid', 'bldgid', 'suitid', 'occpname', 'values')
	ordering = ('bldgid',)
	search_fields = ('bldgid',)
	list_filter = ('bldgid',)

@admin.register(LogDatosP)
class LogDatosAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'building', 'created', 'real')
	ordering = ('created',)
