from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200 )
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['name']





