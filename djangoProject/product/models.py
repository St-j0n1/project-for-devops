from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, help_text='Title of the product')
    price = models.DecimalField(decimal_places=2, help_text='Price of the product'),
    description = models.TextField(help_text='Description of the product', blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

