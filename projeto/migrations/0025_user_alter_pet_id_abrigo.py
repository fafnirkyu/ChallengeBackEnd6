# Generated by Django 4.1.7 on 2023-04-06 04:16

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projeto", "0024_alter_pet_id_abrigo"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                    "username",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z_ áàâãéèêíïóôõöúçñ]*$",
                                "Não inclua números neste campo",
                            )
                        ],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email"
                    ),
                ),
                ("passwor1", models.CharField(max_length=35)),
                ("password2", models.CharField(max_length=35)),
                (
                    "date_joined",
                    models.DateField(
                        verbose_name=datetime.datetime(2023, 4, 6, 1, 16, 5, 941546)
                    ),
                ),
                ("is_tutor", models.BooleanField(default=False)),
                ("is_shelter", models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name="pet",
            name="id_abrigo",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="projeto.abrigo",
            ),
        ),
    ]
