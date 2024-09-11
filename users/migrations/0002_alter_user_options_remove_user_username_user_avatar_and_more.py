# Generated by Django 5.1.1 on 2024-09-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Your photo",
                null=True,
                upload_to="users/avatars",
                verbose_name="Avatar",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Your city",
                max_length=25,
                null=True,
                verbose_name="City",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Your phone number",
                max_length=35,
                null=True,
                verbose_name="Phone",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Your email address",
                max_length=254,
                unique=True,
                verbose_name="Email",
            ),
        ),
    ]
