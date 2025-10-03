from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    sluglink = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantitys = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)  #blank = true pour avoir une description facultative
    picture = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantitys})"





class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #plusieur à 1 = plusieur article relier a 1 utilisateur
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)


    def __str__(self):
        return f"{self.user.username}"

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        
        super().delete(*args, **kwargs)
# Create your models here.
