from abc import ABC

from rest_framework import serializers
from .models import Movie, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import BaseSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'num_of_ratings', 'avg_rating']
        # extra_fields = ('num_of_ratings',)
    # def create(self, validated_data):
    #     movie = Movie.objects.create(**validated_data)
    #     return movie
    #


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = "__all__"
