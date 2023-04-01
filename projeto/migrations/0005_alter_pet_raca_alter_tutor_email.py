# Generated by Django 4.1.7 on 2023-04-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projeto", "0004_pet_raca"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet", name="raca", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
