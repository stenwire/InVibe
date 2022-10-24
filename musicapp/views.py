from functools import partial
from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, render
from .models import Artiste
from .models import Song
from .models import Lyric
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import ArtisteSerializer
from .serializers import SongSerializer
from .serializers import LyricSerializer
from musicapp import serializers

# Create your views here.

# ------------ Artiste View Handler ------------ #
class ArtisteListView(APIView):
    def get(self, request, *args, **kwargs):
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArtisteDetailView(APIView):
    def get_artist(self, id, *args):
        try:
            return Artiste.objects.get(id=id)
        except Artiste.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        artist = self.get_artist(id, request.user.id)
        if not artist:
            return Response(
                {"message": f"Artist with ID:{id} not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ArtisteSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id, *args, **kwargs):
        artist = self.get_artist(id, request.user.id)
        if not artist:
            return Response(
                {"message": f"Artiste with ID:{id} not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'age': request.data.get('age'),
        }

        serializer = SongSerializer(instance=artist, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, *args, **kwargs):
        artist = self.get_artist(id, request.user.id)
        if not artist:
            return Response(
                {"message": f"Artiste with ID:{id} not found!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        artist.delete()

        return Response(
                {"message": f"Artiste with ID:{id} have been deleted!"},
                status=status.HTTP_200_OK
            )


# ------------ Song View Handler ------------ #
class SongListView(APIView):
    def get(self, request, *args, **kwargs):
        songs = Song.objects.order_by('date_released')
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id, *args, **kwargs):
        song = self.get_song(id, request.user.id)
        if not song:
            return Response(
                {"message": f"Song with {id} not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'title': request.data.get('title'),
        }

        serializer = SongSerializer(instance=song, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SongDetailView(APIView):
    def get_song(self, id, *args):
        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            return None

    def get(self, request, id, *args, **kwargs):
        song = self.get_song(id, request.user.id)
        if not song:
            return Response(
                {"message": f"Song with ID:{id} not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id, *args, **kwargs):
        song = self.get_song(id, request.user.id)
        if not song:
            return Response(
                {"message": f"Song with ID:{id} not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = {
            'title': request.data.get('title'),
        }

        serializer = SongSerializer(instance=song, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, *args, **kwargs):
        song = self.get_song(id, request.user.id)
        if not song:
            return Response(
                {"message": f"Song with ID:{id} not found!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        song.delete()

        return Response(
                {"message": f"Song with ID:{id} have been deleted!"},
                status=status.HTTP_200_OK
            )


# ------------ Lyrics View Handler ------------ #
class LyricDetailView(APIView):
    def get_lyric(self, song_id):
        try:
            return Lyric.objects.get(song_id=song_id)
        except Lyric.DoesNotExist:
            return None

    def get(self, request, song_id, *args, **kwargs):
        lyrics = self.get_lyric(song_id)
        if not lyrics:
            return Response(
                {"message": f"Lyrics for ID:{song_id} not found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LyricSerializer(lyrics)
        return Response(serializer.data, status=status.HTTP_200_OK)
