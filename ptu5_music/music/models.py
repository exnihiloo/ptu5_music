from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Band(models.Model):
    name = models.CharField(_("name"), max_length=150)

    def __str__(self):
        return self.name


class Album(models.Model):
    band = models.ForeignKey(
        Band, 
        verbose_name=_("band"), 
        on_delete=models.CASCADE,
        related_name="albums"
    )
    name = models.CharField(_("name"), max_length=150)
    
    def __str__(self):
        return f"{self.name} ({self.band})"


class Song(models.Model):
    album = models.ForeignKey(
        Album,
        verbose_name=_("album"), 
        on_delete=models.CASCADE,
        related_name="songs"
    )
    name = models.CharField(_("name"), max_length=150)
    duration = models.DurationField(_("duration"))

    def __str__(self):
        return f"{self.name} - {self.duration} ({self.album})"

class AlbumReview(models.Model):
    VALUE = (
    (1, "Score 1"),
    (2, "Score 3"),
    (3, "Score 4"),
    (4, "Score 4"),
    (5, "Score 5"),
    (6, "Score 6"),
    (7, "Score 7"),
    (8, "Score 8"),
    (9, "Score 9"),
    (10, "Score 10"),
)
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name="album_reviews"
    )
    album = models.ForeignKey(
        Album, 
        verbose_name=_("album"), 
        on_delete=models.CASCADE,
        related_name="album_reviews"
    )
    content = models.TextField(_("content"), max_length=2000)
    score = models.PositiveSmallIntegerField(_("score"), default = 0, choices=VALUE)
    image = models.ImageField(_("image"), upload_to = "user_images/", blank = True, null = True)


    def __str__(self):
        return f"{self.album} - {self.content}"


class AlbumReviewComment(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name="album_review_comments"
    )
    album_review = models.ForeignKey(
        AlbumReview,
        verbose_name=_("album_review"),
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField(_("content"), max_length=2000)
    image = models.ImageField(_("image"), upload_to = "user_images/", blank = True, null = True)

    def __str__(self):
        return f"{self.album_review} : {self.content}"


class AlbumReviewLike(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name="album_review_likes"
    )
    album_review = models.ForeignKey(
        AlbumReview, 
        verbose_name=_("album_review"),
        on_delete=models.CASCADE,
        related_name="likes"
    )

    def __str__(self):
        return f"{self.user} likes {self.album_review}"
    