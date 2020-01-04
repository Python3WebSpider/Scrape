from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from ..models import Movie
from ..serializers import MovieSerializer

def movie(request, page=1):
    return render(request, 'movie/index.html')

class MovieListCreateViewSet(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieRetrieveUpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
