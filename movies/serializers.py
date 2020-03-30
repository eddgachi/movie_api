from rest_framework import serializers
from movies.models import Movie, Actor, Director


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'likes',
            'unlikes',
            'release_year',
            'actors',
            'directors'
        ]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'name',
        ]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            'name',
        ]
