# Generated by Django 4.2.6 on 2023-11-01 12:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_rename_year_producto_stock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='El valor del rating no puede ser menor que 0.'), django.core.validators.MaxValueValidator(5, message='El valor del rating no puede ser mayor que 5.')])),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
