from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)  #blank = true pour avoir une description facultative
    picture = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}"

# Create your models here.
