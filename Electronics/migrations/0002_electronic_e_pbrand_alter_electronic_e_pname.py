# Generated by Django 4.1.7 on 2023-03-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronic',
            name='e_pbrand',
            field=models.CharField(choices=[('S', 'SYSKA'), ('L', 'LG'), ('W', 'Whirlpool'), ('B', 'Bajaj')], default='Bajaj', max_length=40),
        ),
        migrations.AlterField(
            model_name='electronic',
            name='e_pname',
            field=models.CharField(choices=[('T', 'Tubelight'), ('F', 'Fridge'), ('TV', 'Television'), ('M', 'Mixer')], max_length=40),
        ),
    ]
