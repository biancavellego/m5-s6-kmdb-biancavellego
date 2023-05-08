# Generated by Django 4.1 on 2023-05-08 18:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0005_alter_review_stars"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        1,
                        message={
                            "starts": "Ensure this value is less than or equal to 5."
                        },
                    ),
                    django.core.validators.MaxValueValidator(
                        5,
                        message={
                            "starts": "Ensure this value is less than or equal to 5."
                        },
                    ),
                ],
            ),
        ),
    ]
