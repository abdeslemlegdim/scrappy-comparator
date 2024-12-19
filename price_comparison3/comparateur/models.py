from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)
    class Meta:
        db_table = 'tunisia_net'

    def __str__(self):
        return self.title
