# Generated by Django 5.2.3 on 2025-07-25 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "Medicine_inventory",
            "0003_alter_medicine_batch_number_alter_medicine_category",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicineAction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        choices=[
                            ("added", "Added"),
                            ("updated", "Updated"),
                            ("deleted", "Deleted"),
                        ],
                        max_length=10,
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Medicine_inventory.medicine",
                    ),
                ),
            ],
        ),
    ]
