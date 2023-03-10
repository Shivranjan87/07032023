# Generated by Django 4.1.7 on 2023-03-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_pname', models.CharField(choices=[('T', 'Tube-light'), ('F', 'Fridge'), ('TV', 'Television'), ('M', 'Mixer')], max_length=40)),
                ('e_pid', models.IntegerField()),
                ('e_pprice', models.FloatField()),
                ('e_pwarr', models.IntegerField()),
            ],
            options={
                'db_table': 'electric',
            },
        ),
    ]
