# Generated by Django 4.1.7 on 2023-03-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wadrobe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wadrobe',
            name='w_wcolor',
            field=models.CharField(default='white', max_length=10),
        ),
    ]