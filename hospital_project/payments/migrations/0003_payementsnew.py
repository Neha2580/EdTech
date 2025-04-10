# Generated by Django 5.1.6 on 2025-04-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0002_alter_payments_consultationfee"),
    ]

    operations = [
        migrations.CreateModel(
            name="payementsnew",
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
                ("Name", models.CharField(max_length=255)),
                ("Remarks", models.CharField(max_length=255)),
                ("consultationFee", models.IntegerField(null=True)),
            ],
        ),
    ]
