# Generated by Django 5.1.1 on 2024-09-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_contact"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"verbose_name": "Контакты", "verbose_name_plural": "Контакты"},
        ),
        migrations.AlterField(
            model_name="contact",
            name="country",
            field=models.CharField(
                default="Российская Федерация",
                help_text="Введите наименование страны",
                max_length=50,
                verbose_name="Страна",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="tax_reg_number",
            field=models.CharField(
                blank=True,
                help_text="Введите номер налогоплательщика",
                max_length=12,
                null=True,
                verbose_name="ИНН",
            ),
        ),
    ]
