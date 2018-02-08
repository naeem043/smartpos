from django.db import models

# Create your models here.

# class product(models.Model):
#     product_name = models.CharField(max_length=150)
#     status = models.BooleanField(default=1)

class MenuInfo(models.Model):
    menu_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100,blank=True)
    module = models.CharField(max_length=100, blank=True)
    page_name = models.CharField(max_length=100, blank=True)
    parent = models.IntegerField(blank=True)
    menu_order = models.IntegerField(blank=True)
    status = models.BooleanField(default=1,blank=True)


