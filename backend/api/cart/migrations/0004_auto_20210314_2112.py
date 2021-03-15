# Generated by Django 3.1.7 on 2021-03-14 15:42
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0003_auto_20210314_2107"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productrating",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="p_id",
                to="cart.product",
            ),
        ),
    ]
