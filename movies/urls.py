from django.urls import path

from movies.views import MovieView
from reviews.views import ReviewView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<uuid:movie_id>/reviews/", ReviewView.as_view()),
]
