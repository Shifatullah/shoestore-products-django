from django.db import models

# Create your models here.

class Product(models.Model):
    # product name
    name = models.CharField(max_length=255, null=False)

    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return "{} - is - {}".format(self.name, self.name)