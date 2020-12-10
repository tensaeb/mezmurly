from rest_framework import generics, permissions

from .models import Artist, Album, Track

from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

# Create your views here.


class ArtistList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
