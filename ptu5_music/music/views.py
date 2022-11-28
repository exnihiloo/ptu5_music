from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from . import models, serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class BandList(generics.ListCreateAPIView):
    queryset = models.Band.objects.all()
    serializer_class = serializers.BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class AlbumList(generics.ListCreateAPIView):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class SongList(generics.ListCreateAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


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
        review = models.AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review=review)

    def get_queryset(self):
        review = models.AlbumReview.objects.get(pk=self.kwargs['pk'])
        return models.AlbumReviewComment.objects.filter(album_review=review)


class AlbumReviewLikeCreate(generics.CreateAPIView):
    # queryset = models.AlbumReviewLike.objects.all()
    serializer_class = serializers.AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        album_review = models.AlbumReview.objects.get(pk = self.kwargs["pk"])
        return models.AlbumReviewLike.objects.filter(user = user, album_review = album_review)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError(_('You already left like on this review!'))
        user = self.request.user
        album_review = models.AlbumReview.objects.get(pk = self.kwargs["pk"])
        serializer.save(user = user, album_review = album_review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError(_("You didn't like this review to begin with."))



    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AlbumReview.objects.all()
    serializer_class = serializers.AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def delete(self, request, *args, **kwargs):
        album_review = models.AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_("You can't delete reviews not of your own!!!"))


    def put(self, request, *args, **kwargs):
        album_review = models.AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_("You can't update reviews that are not yours."))


class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AlbumReviewComment.objects.all()
    serializer_class = serializers.AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def delete(self, request, *args, **kwargs):
        comment = models.AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_("You can't delete comments not of your own!!!"))


    def put(self, request, *args, **kwargs):
        comment = models.AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_("You can't update comments that are not yours."))


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(pk = self.request.user.pk)
        if user.exists():
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('User doesn\'t exist.')