from rest_framework import serializers
from . import models

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ('id', 'name', 'user', 'user_id')


class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source='band.name')
    class Meta:
        model = models.Album
        fields = ('id', 'name', 'band', 'band_name') 


class SongSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source='album.name')
    class Meta:
        model = models.Song
        fields = ('id', 'name', 'duration', 'album_name')


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_name = serializers.ReadOnlyField(source='album.name')
    class Meta:
        model = models.AlbumReview
        fields = ('id', 'album', 'album_name', 'content', 'score', 'user', 'user_id')

class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='album_review.content')
    album_name = serializers.ReadOnlyField(source='album_review.album.name')
    class Meta:
        model = models.AlbumReviewComment
        fields = ('id', 'album_review', 'content', 'user', 'user_id', 'album_name')


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='album_review.score')
    album_name = serializers.ReadOnlyField(source='album_review.album.name')
    class Meta:
        model = models.AlbumReviewLike
        fields = ('id', 'album_review', 'album_name', 'user', 'user_id',)