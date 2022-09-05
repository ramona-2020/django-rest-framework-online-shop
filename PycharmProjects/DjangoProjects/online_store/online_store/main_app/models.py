from django.db import models


class Product(models.Model):

    title = models.CharField(
        max_length=30,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return self.title


class Order(models.Model):

    date = models.DateField()
    filter_fields = []
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['date', ]
