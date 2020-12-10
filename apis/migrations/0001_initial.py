# Generated by Django 3.1.4 on 2020-12-10 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_title', models.CharField(max_length=100)),
                ('release_date', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('album_pic', models.ImageField(upload_to='album_pics')),
                ('album_type', models.CharField(choices=[('Single', 'Single'), ('Album', 'Album'), ('Compilation', 'Compilation'), ('Remix', 'Remix'), ('Live', 'Live')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('track_title', models.CharField(max_length=150)),
                ('track_body', models.TextField()),
                ('track_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.album')),
                ('track_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.artist')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='album_artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.artist'),
        ),
    ]
