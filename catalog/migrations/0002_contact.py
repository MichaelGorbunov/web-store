# Generated by Django 5.1.1 on 2024-09-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                    "country",
                    models.CharField(
                        help_text="Введите наименование страны",
                        max_length=50,
                        verbose_name="Страна",
                    ),
                ),
                (
                    "tax_reg_number",
                    models.CharField(
                        blank=True,
                        help_text="Введите номер налогоплательщика",
                        max_length=12,
                        null=True,
                        verbose_name="Номер налогоплательщика",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        help_text="Введите адрес", max_length=250, verbose_name="Адрес"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        help_text="Введите номер телефона",
                        max_length=12,
                        verbose_name="Основной телефон",
                    ),
                ),
            ],
            options={
                "verbose_name": "ИНН",
                "verbose_name_plural": "ИНН",
            },
        ),
    ]
