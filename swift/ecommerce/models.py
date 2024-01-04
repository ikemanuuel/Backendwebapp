from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Item(models.Model):
    items_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    size = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank = True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name

