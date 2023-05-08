# Generated by Django 4.1 on 2023-05-08 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_alter_review_options_review_critic_review_movie_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                default=1,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
