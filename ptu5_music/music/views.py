from django.shortcuts import render
from rest_framework import generics, permissions
from . import models, serializers

class BandList(generics.ListCreateAPIView):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumList(generics.ListCreateAPIView):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SongList(generics.ListCreateAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = models.AlbumReview.objects.all()
    serializer_class = serializers.AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewCommentList(generics.ListCreateAPIView):
    queryset = models.AlbumReviewComment.objects.all()
    serializer_class = serializers.AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewLikeList(generics.ListCreateAPIView):
    queryset = models.AlbumReviewLike.objects.all()
    serializer_class = serializers.AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)