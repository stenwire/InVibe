from datetime import datetime
from django.db import models

# Create your models here.


class Artiste(models.Model):
    """A model containing artiste details

    Attributes:
        first_name  The artiste first name
        last_name   The artiste last name
        age         The artiste age
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __repr__(self) -> str:
        return f'<{self.first_name}>'


class Song(models.Model):
    """A model containing Song details

    Attributes:
        title               The song name
        date_released       The song release date
        likes               The song likes
        artiste_id          The artiste id
    """
    title = models.CharField(max_length=200)
    date_released = models.DateField('date released', default=datetime.now)
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f'<{self.title}>, <{self.artiste_id}>'


class Lyric(models.Model):
    """A model containing Lyric details

    Attributes:
        content   The entire song content
        song_id   The song id
    """
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f'<{self.content}>, <{self.song_id}>'
