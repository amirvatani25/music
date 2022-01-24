
from django.shortcuts import render
from musicbeats.models import Singer , Hesohal , Song , Category , Album
# Create your views here.

def homepage(request):
    singers = Singer.objects.all()
    hesohals = Hesohal.objects.all()
    songs = Song.objects.all()
    categorys= Category.objects.all()
    albums = Album.objects.all()

    context = {'singers':singers, 'hesohals':hesohals,
               'songs':songs, 'categorys':categorys,
               'albums':albums,}
    return render(request, 'homepage.html',context)
