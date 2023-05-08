from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Review, validate_stars
from users.models import User
from movies.models import Movie

class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
        ]

class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    stars = serializers.IntegerField(validators=[validate_stars], allow_null=True)


    def create(self, validated_data: dict) -> Review:
        movie_id = get_object_or_404(Movie, pk=validated_data["movie_id"])

        return Review.objects.create(**validated_data)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
        ]
        depth = 1

        read_only_fields = ["id", "movie_id", "critic"]

        extra_kwargs = {
            "spoilers": {"allow_null": True},
            "stars": {"allow_null": True},
        }
