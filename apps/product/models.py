from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    price = models.BigIntegerField('price')
