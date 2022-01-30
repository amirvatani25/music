from django.contrib import admin
from .models import Song , Tag ,Review ,Album , Category , Playlist, Singer,Hesohal,AdminPlaylist
# Register your models here.


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Playlist)
admin.site.register(Singer)
admin.site.register(Hesohal)
admin.site.register(AdminPlaylist)

