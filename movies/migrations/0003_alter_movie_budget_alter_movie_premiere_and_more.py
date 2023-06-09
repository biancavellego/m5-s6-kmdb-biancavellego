# Generated by Django 4.1 on 2023-05-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_movie_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="budget",
            field=models.DecimalField(decimal_places=2, default=None, max_digits=12),
        ),
        migrations.AlterField(
            model_name="movie",
            name="premiere",
            field=models.DateField(default=None, max_length=127),
        ),
        migrations.AlterField(
            model_name="movie",
            name="title",
            field=models.CharField(default=None, max_length=127),
        ),
    ]
