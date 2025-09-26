from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)  #blank = true pour avoir une description facultative
    picture = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

# Create your models here.
