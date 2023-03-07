from django.db import models


# Create your models here.

class wadrobe(models.Model):
    w_wname = models.CharField(max_length=40)
    w_wbrand = models.CharField(max_length=50, choices=[('H', 'Horse_villa'), ('D', 'Denim')])
    w_wid = models.IntegerField()
    w_wcolor = models.CharField(max_length=10, default='white')
    w_wprice = models.FloatField()
    w_wwarr = models.IntegerField()

    class Meta:
        db_table = 'wadrobe'
