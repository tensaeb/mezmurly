from rest_framework import serializers

from .models import Artist, Album, Track


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Artist


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Album


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Track
