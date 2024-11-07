# Generated by Django 5.1.2 on 2024-11-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='unit',
            field=models.CharField(choices=[('kg', 'Kilograms'), ('g', 'Grams'), ('L', 'Liters'), ('ml', 'Milliliters'), ('pcs', 'Pieces'), ('doz', 'dozen')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, help_text='Price per unit', max_digits=10, null=True),
        ),
    ]