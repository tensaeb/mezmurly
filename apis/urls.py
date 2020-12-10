from django.urls import path
from .views import AlbumList, AlbumDetail, ArtistList, ArtistDetail, TrackList, TrackDetail

urlpatterns = [
    path('artists/', ArtistList.as_view()),
    path('artists/<int:pk>/', ArtistDetail.as_view()),


    path('albums/', AlbumList.as_view()),
    path('albums/<int:pk>/', AlbumDetail.as_view()),

    path('tracks/', TrackList.as_view()),
    path('tracks/<int:pk>/', TrackDetail.as_view()),
]
