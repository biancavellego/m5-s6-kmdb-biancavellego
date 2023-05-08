from rest_framework import serializers

from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewSerializer(serializers.ModelSerializer):
    critic = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Review:
        return Review.objects.create(**validated_data)

    def get_critic(self, obj):
        return {
            "id": obj.user.id,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
        }

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id ",
            "critic",
        ]
        depth = 1

        read_only_fields = ["id", "movie_id", "critic"]

        extra_kwargs = {
            "spoilers": {"allow_null": True},
        }
