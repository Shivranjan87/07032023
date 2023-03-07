from django.db import models


# Create your models here.

class electronic(models.Model):
    e_pname = models.CharField(max_length=40, choices=[('T', 'Tubelight'), ('F', 'Fridge'), ('T', 'Television'), ('M', 'Mixer')])
    e_pid = models.IntegerField()
    e_pprice = models.FloatField()
    e_pbrand = models.CharField(max_length=40, choices=[('S', 'SYSKA'), ('L', 'LG'), ('W', 'Whirlpool'), ('B', 'Bajaj')])
    e_pwarr = models.IntegerField()

    class Meta:
        db_table = 'electric'
