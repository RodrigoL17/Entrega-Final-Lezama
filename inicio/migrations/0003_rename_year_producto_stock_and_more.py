# Generated by Django 4.2.6 on 2023-11-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_paleta_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='year',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='brand',
            new_name='title',
        ),
        migrations.AddField(
            model_name='producto',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]