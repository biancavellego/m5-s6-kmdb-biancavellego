from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrCriticOrReadOnly

from reviews.models import Review
from reviews.serializers import ReviewSerializer

class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCriticOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"    

    def perform_create(self, serializer: ReviewSerializer) -> None:
        serializer.save(critic=self.request.user, movie_id=self.kwargs["movie_id"])
