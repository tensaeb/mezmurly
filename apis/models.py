from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=150)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    TYPES = (
        ('Single', 'Single'),
        ('Album', 'Album'),
        ('Compilation', 'Compilation'),
        ('Remix', 'Remix'),
        ('Live', 'Live'),
    )

    album_id = models.AutoField(primary_key=True)
    album_title = models.CharField(max_length=100)
    album_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.PositiveSmallIntegerField(blank=True, null=True)
    album_pic = models.ImageField(upload_to='album_pics')
    album_type = models.CharField(max_length=11, choices=TYPES)

    def __str__(self):
        return self.album_title


class Track(models.Model):

    track_id = models.AutoField(primary_key=True)
    track_title = models.CharField(max_length=150)
    track_body = models.TextField()
    track_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.track_title
