import uuid

from django.db import models

class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=127)
    duration = models.DurationField()
    premiere = models.DateField(max_length=127)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    overview = models.TextField(null=True)

    class Meta:
        ordering = ("title",)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )
