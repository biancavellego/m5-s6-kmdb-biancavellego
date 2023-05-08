import uuid

from django.db import models
from django.core.exceptions import ValidationError

def validate_stars(value):
    if value > 5:
        raise ValidationError("Ensure this value is less than or equal to 5.")
    if value < 1:
           raise ValidationError("Ensure this value is greater than or equal to 1.")

class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.IntegerField(default=1, validators=[validate_stars], null=True)
    review = models.TextField()
    spoilers = models.BooleanField(null=True, default=False)

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    critic = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    class Meta:
        ordering = ("review",)
