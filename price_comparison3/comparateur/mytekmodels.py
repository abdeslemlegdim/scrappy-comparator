from djongo import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=255)
    class Meta:
        db_table = 'MyTek'  # Nom de la collection dans MongoDB
    def __str__(self):
        return self.title
