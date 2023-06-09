# from rest_framework.pagination import PageNumberPagination
# from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdminOrCreate


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreate]

    serializer_class = UserSerializer
    queryset = User.objects.all()


# class UserView(APIView, PageNumberPagination):
#     def get(self, request: Request) -> Response:
#         """
#         Listagem de usuários
#         """
#         users = User.objects.all()
#         result_page = self.paginate_queryset(users, request)
#         serializer = UserSerializer(result_page, many=True)

#         return self.get_paginated_response(serializer.data)

#     def post(self, request: Request) -> Response:
#         """
#         Registro de usuários
#         """
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data, status.HTTP_201_CREATED)
