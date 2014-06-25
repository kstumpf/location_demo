from django.db import models
from locations.models import Location

# Create your models here.
class Proverb(models.Model):
    proverb = models.CharField(max_length = 300)
    culture = models.ForeignKey(Location, limit_choices_to={'type': 'culture'}, related_name='cultureprov', blank=True, null=True)
    continent = models.ForeignKey(Location, limit_choices_to={'type': 'continent'}, related_name='continentprov', blank=True, null=True)
    country = models.ForeignKey(Location, limit_choices_to={'type': 'country'}, related_name='countryprov', blank=True, null=True)

    def __unicode__(self):
        return self.proverb
