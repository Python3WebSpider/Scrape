from rest_framework.serializers import ModelSerializer
from .models import Movie

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'actors', 'url', 'cover', 'score', 'duration', 'country', 'released_at']
