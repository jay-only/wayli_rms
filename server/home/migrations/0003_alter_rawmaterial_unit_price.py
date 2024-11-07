# Generated by Django 5.1.2 on 2024-11-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rawmaterial_price_alter_rawmaterial_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Price per unit', max_digits=10, null=True),
        ),
    ]