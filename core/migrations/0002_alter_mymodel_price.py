# Generated by Django 3.2.6 on 2022-01-24 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]