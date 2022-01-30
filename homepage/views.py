
from django.shortcuts import render
from musicbeats.models import Singer , Hesohal , Song , Category , Album ,AdminPlaylist
# Create your views here.

def homepage(request):
    singers = Singer.objects.all()
    hesohals = Hesohal.objects.all()
    songs = Song.objects.all()
    categorys= Category.objects.all()
    albums = Album.objects.all()
    adminPlaylists = AdminPlaylist.objects.all()

    context = {'singers':singers, 'hesohals':hesohals,
               'songs':songs, 'categorys':categorys,
               'albums':albums,'adminPlaylists':adminPlaylists}
    return render(request, 'homepage.html',context)
