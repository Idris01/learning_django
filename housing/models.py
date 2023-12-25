from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(
            max_length=50,
            help_text="name of the house",
            blank=False,
            null=False)
    description = models.TextField()
    country = models.CharField(
            max_length=200,
            help_text="country of location",
            blank=False,
            null=False)
    image = models.FileField()

