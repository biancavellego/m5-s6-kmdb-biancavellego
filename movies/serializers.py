from rest_framework import serializers

from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, allow_null=True)

    def create(self, validated_data: dict) -> Movie:
        genres_data = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)

        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(name=genre_data["name"])
            movie.genres.add(genre)

        return movie

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]
        depth = 2

        read_only_fields = ["id"]

        extra_kwargs = {
            "genres": {"allow_null": True},
        }