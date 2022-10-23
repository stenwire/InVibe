from django.contrib import admin

# Register your models here.

from .models import Artiste
from .models import Song
from .models import Lyric

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyric)
