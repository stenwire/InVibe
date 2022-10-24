from django.urls import path
from .views import (
    SongListView,
    SongDetailView,
    ArtisteListView,
    ArtisteDetailView,
    LyricDetailView,
)

app_name = 'musicapp'

urlpatterns = [
    path('songs/', SongListView.as_view()),
    path('artistes/', ArtisteListView.as_view()),
    path('artistes/<int:id>/', ArtisteDetailView.as_view()),
    path('songs/<int:id>/', SongDetailView.as_view()),
    path('songs/<int:song_id>/lyrics', LyricDetailView.as_view()),
    ]
