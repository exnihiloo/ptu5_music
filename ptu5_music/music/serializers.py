from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ('id', 'name',)


class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source='band.name')
    class Meta:
        model = models.Album
        fields = ('id', 'name', 'band', 'band_name') 


class SongSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source='album.name')
    class Meta:
        model = models.Song
        fields = ('id', 'name', 'duration', 'album_name', 'album')


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review_content = serializers.ReadOnlyField(source='album_review.content')
    album_name = serializers.ReadOnlyField(source='album_review.album.name')
    class Meta:
        model = models.AlbumReviewComment
        fields = ('id', 'album_review', 'content', 'image', 'album_review_content', 'user', 'user_id', 'album_name')


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_name = serializers.ReadOnlyField(source='album.name')
    comments_count = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments = AlbumReviewCommentSerializer(many=True, read_only = True)
    
    class Meta:
        model = models.AlbumReview
        fields = ('id', 'album', 'album_name', 'content', 'image', 'score', 'user', 'user_id', 'comments_count', 'comments', 'likes_count')

    def get_comments_count(self, obj):
        return models.AlbumReviewComment.objects.filter(album_review=obj).count()


    def get_likes_count(self, obj):
        return models.AlbumReviewLike.objects.filter(album_review=obj).count()


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # user_id = serializers.ReadOnlyField(source='user.id')
    # album_review_score = serializers.ReadOnlyField(source='album_review.score')
    # album_name = serializers.ReadOnlyField(source='album_review.album.name')
    class Meta:
        model = models.AlbumReviewLike
        fields = ('id',) #'album_review_score', 'album_name', 'user', 'user_id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
       