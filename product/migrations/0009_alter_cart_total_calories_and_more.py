# Generated by Django 4.2 on 2024-04-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_calories',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_carbohydrates',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_lipids',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_protein',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_water',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=8),
        ),
    ]
