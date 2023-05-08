from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from rest_framework import generics

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_url_kwarg = "movie_id"

    def perform_create(self, serializer: MovieSerializer) -> None:
        serializer.save(user_id=self.request.user.id)
