# Generated by Django 4.2.6 on 2023-11-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='avater',
            field=models.ImageField(blank=True, null=True, upload_to='avaters'),
        ),
    ]