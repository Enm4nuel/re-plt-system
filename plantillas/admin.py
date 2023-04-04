from django.contrib import admin
from .models import Plantilla

@admin.register(Plantilla)
class PlantillaAdmin(admin.ModelAdmin):
	list_display = ('id', 'bldgid', 'currcode', 'inccat', 'descrptn')
	ordering = ('bldgid',)
	search_fields = ('inccat', 'descrptn', 'currcode', 'bldgid')
	list_filter = ('inccat',)

# Register your models here.
#admin.site.register(Plantilla)