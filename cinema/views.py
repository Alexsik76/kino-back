from rest_framework import viewsets

from .models import Movie, Hall
from .serializers import MovieSerializer, HallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer
    # permission_classes = [permissions.IsAuthenticated]


class HallViewSet(viewsets.ModelViewSet):
    queryset = Hall.objects.all().order_by('name')
    serializer_class = HallSerializer
    # permission_classes = [permissions.IsAuthenticated]
