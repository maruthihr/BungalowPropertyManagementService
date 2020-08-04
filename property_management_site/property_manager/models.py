from django.db import models


class AreaUnit(models.TextChoices):
    SQFT = 'SqFt'

class HomeType(models.TextChoices):
    SINGLEFAMILY = 'SingleFamily'
    APARTMENT = 'Apartment'
    CONDOMINIUM = 'Condominium'
    DUPLEX = 'Duplex'
    MISCELLANEOUS = 'Miscellaneous'
    MULTIFAMILY2TO4 = 'MultiFamily2To4'
    VACANTRESIDENTIALLAND = 'VacantResidentialLand'


# Create your models here.
class Property(models.Model):
    area_unit = models.CharField('AreaUnit', max_length=32, choices=AreaUnit.choices, default=AreaUnit.SQFT)
    bathrooms = models.DecimalField('Bathrooms', max_digits=3, decimal_places=1, null=True)
    bedrooms = models.PositiveIntegerField('Bedrooms')
    home_size = models.PositiveIntegerField('Home Size', null=True)
    home_type = models.CharField('HomeType', max_length=32, choices=HomeType.choices, default=HomeType.SINGLEFAMILY)
    last_sold_date = models.DateField(blank=True, null=True, )
    last_sold_price = models.PositiveIntegerField(blank=True, null=True)
    link = models.CharField(max_length=256)
    price = models.CharField(max_length=16)
    # price = models.DecimalField('Price', max_digits=5, decimal_places=2, null=True, blank=True)
    property_size = models.PositiveIntegerField('Property Size', null=True)
    rent_price = models.DecimalField('Rent Price', max_digits=5, decimal_places=2, null=True, blank=True)
    rentzestimate_amount = models.PositiveIntegerField()
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.PositiveIntegerField()
    tax_year = models.PositiveIntegerField(max_length=4)
    year_built = models.PositiveIntegerField(max_length=4)
    zestimate_amount = models.PositiveIntegerField()
    zestimate_last_updated = models.DateField(blank=True, null=True)
    zillow_id = models.PositiveIntegerField(unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=16)


    def __str__(self):
        return str(self.zillow_id) +'-'+ str(self.last_sold_date)

