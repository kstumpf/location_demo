from django.contrib import admin
from .models import Proverb

class ProverbAdmin(admin.ModelAdmin):
	fields = ('proverb', 'culture', 'continent', 'country')
# Register your models here.
admin.site.register(Proverb)