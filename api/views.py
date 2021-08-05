from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from utils.responses import ok, bad_request
from django.contrib.auth.models import User
import json


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        data = request.data
        user = request.user
        obj = self.get_object()
        stars = data.get('stars', None)
        if stars:
            try:
                rating = Rating.objects.get(user=user, movie=pk)
                if stars:
                    rating.stars = stars
                    rating.save()
                    serializer = RatingSerializer(rating, many=False)
                    return ok(data=serializer.data, result=1, message_code='Updated Successfully!')
            except Exception:
                if stars:
                    rating = Rating.objects.create(movie=obj, user=user, stars=stars)
                    serializer = RatingSerializer(rating, many=False)
                    return ok(data=serializer.data, result=1, message_code='Created Successfully!')
        else:
            return bad_request(data={}, result=-1, message_code='You need provide stars!')
    # def create(self, request, *args, **kwargs):
    #     return super(MovieViewSet, self).create(request, *args, **kwargs)


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
