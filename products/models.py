from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', related_name='products')
    image = models.ImageField(upload_to='products', null=True, blank=True)
    similar_product = models.ManyToManyField(
        'Product',
        null=True, blank=True,
        symmetrical=False
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
