# Generated by Django 4.1.7 on 2023-03-07 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0006_alter_electronic_e_pname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electronic',
            name='e_pwarr',
        ),
    ]
