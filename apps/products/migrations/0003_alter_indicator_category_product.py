# Generated by Django 4.1.2 on 2022-10-07 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_historicalproduct_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Indicador de oferta'),
        ),
    ]
