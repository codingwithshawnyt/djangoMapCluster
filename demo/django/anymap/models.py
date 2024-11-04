from django.contrib.gis.db import models  # Import GIS-specific models from Django

from django.utils.translation import gettext_lazy as _  # Import lazy translation function for internationalization

# Tuple defining different styles of gardens, used for choices in a model field
GARDEN_STYLES = (
    ('imperial', _('imperial')),
    ('japanese', _('japanese')),
    ('stone', _('stone')),
    ('flower', _('flower')),
    ('other', _('other')),
)

class Owner(models.Model):
    # Model representing an owner of a garden
    name = models.CharField(max_length=255)  # Name field with a maximum length of 255 characters

class Gardens(models.Model):
    # Model representing a garden
    connection_name = "default"  # Database connection name, defaults to 'default'
    name = models.CharField(max_length=255)  # Name of the garden
    style = models.CharField(max_length=20, choices=GARDEN_STYLES)  # Style of the garden, with predefined choices
    rating = models.PositiveIntegerField()  # Rating of the garden as a positive integer
    free_entrance = models.BooleanField(default=False)  # Boolean field indicating if entrance is free
    last_renewal = models.DateTimeField()  # Date and time of the last renewal
    coordinates = models.PointField(srid=3857)  # GIS point field for garden coordinates

    owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE)  # Foreign key to the Owner model, nullable

    def __str__(self):
        # String representation of the Gardens model
        return '{0} ({1})'.format(self.name, self.style)

    class Meta:
        # Meta options for the Gardens model
        ordering = ('pk',)  # Default ordering by primary key