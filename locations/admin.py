from .models import Location
from django.contrib import admin

class LocationAdmin(admin.ModelAdmin):
    fields = ('name', 'type', 'parent', 'overlapswith')

# Register your models here.
admin.site.register(Location)
