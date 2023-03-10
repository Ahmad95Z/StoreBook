# Generated by Django 4.1.7 on 2023-03-06 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_by",
            field=models.ForeignKey(
                default="admin",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
