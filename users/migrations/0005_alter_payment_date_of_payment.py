# Generated by Django 5.1.1 on 2024-09-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_payment_options_alter_payment_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="date_of_payment",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты"),
        ),
    ]
