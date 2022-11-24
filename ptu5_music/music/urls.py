from django.urls import path
from . import views


urlpatterns = [
    path('bands/', views.BandList.as_view()),
    path('albums/', views.AlbumList.as_view()),
    path('songs/', views.SongList.as_view()),
    path('album_reviews/', views.AlbumReviewList.as_view()),
    path('album_review_comments/', views.AlbumReviewCommentList.as_view()),
    path('album_review_likes/', views.AlbumReviewLikeList.as_view()),
]
