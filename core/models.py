# models.py
from django.db import models
from django.utils import timezone


class Word(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

class Image(models.Model):
    image = models.ImageField(upload_to='word_images/', null=True, blank=True)

    # def __str__(self):
    #     return self.word

class ProductDetails(models.Model):
    productId = models.CharField(max_length=20, primary_key=True, db_column='productid')
    category = models.CharField(max_length=20, db_column='category')
    item = models.CharField(max_length=30, db_column='item')
    description = models.CharField(max_length=20, db_column='description')
    units = models.CharField(max_length=10, db_column='units')
    thresholdValue = models.IntegerField(db_column='thresholdvalue')
    image = models.CharField(max_length=255, db_column='image')  # Example, adjust max_length as needed


    class Meta:
        db_table = 'productdetails'



class RequestDetails(models.Model):
    username = models.CharField(max_length=255)
    itemname = models.CharField(max_length=255)
    description = models.TextField()
    required_quantity = models.IntegerField()
    image = models.JSONField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.itemname
