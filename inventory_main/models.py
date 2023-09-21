from django.db import models

class Item(models.Model):
    itemType = models.CharField(max_length=100)
    brandName = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    serialNumber = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.serialNumber  
