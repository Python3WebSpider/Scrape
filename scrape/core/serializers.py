from rest_framework_mongoengine import serializers
from .models import Movie


class MovieSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'actors', 'url', 'cover', 'score', 'duration', 'country', 'released_at']