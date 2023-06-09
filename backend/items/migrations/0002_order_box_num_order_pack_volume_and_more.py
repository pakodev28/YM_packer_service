# Generated by Django 4.2.1 on 2023-06-09 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="box_num",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="pack_volume",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="recommended_cartontype",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="recommended_orders",
                to="items.cartontype",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="sel_calc_cube",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="selected_cartontype",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="selected_orders",
                to="items.cartontype",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="trackingid",
            field=models.UUIDField(
                blank=True, default=uuid.uuid4, editable=False, null=True
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="who",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="whs",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="sku",
            name="goods_wght",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="cargotype",
            name="cargotype",
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name="sku",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
