from django.db import models

# Create your models here.
class Location(models.Model):
    LOCATION_CHOICES = (
        ('culture', 'Culture'),
        ('continent', 'Continent'),
        ('country', 'Country'),
    )
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='country')
    parent = models.ForeignKey('self', related_name = "children", blank=True, null=True)
    overlapswith = models.ManyToManyField("self", related_name = "overlapswith", blank=True)

    def __unicode__(self):
        return self.name

    