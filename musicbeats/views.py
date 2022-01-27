from django.shortcuts import render , redirect
from .models import Singer , Playlist , Song, Hesohal,Album
from .utils import searchSongs,paginationTheSongs,searchSinger,searchHesohal,searchAlbum,paginationTheHesohal,paginationTheAlbum,paginationTheSingers
from django.contrib.auth.decorators import login_required
from .forms import playlistForm




# Create your views here.

def playLists(request):
    playlists=Playlist.objects.all()
    context={
        'playlists':playlists
    }
    return render(request,'musicbeats/playlist.html',context)


def singers(request):
    singers , search_query = searchSinger(request)
    custom_range , singers = paginationTheSingers(request,singers,2)
    context = {'singers':singers , 'search_query':search_query,'custom_range':custom_range}

    return render(request,'musicbeats/archive-singer.html',context)

def singer(request,pk):
    singerObj = Singer.objects.get(id=pk)
    songs = Song.objects.all()
    context={'singer':singerObj,
             'songs':songs,}
    return render(request,'musicbeats/single-singer.html',context)
def play(request,pk):
    songObj=Song.objects.get(id=pk)


    context={
        'song':songObj
    }
    return render(request,'musicbeats/player.html',context)

def single_hesohal(request,pk):
    hesohalObj= Hesohal.objects.get(id=pk)
    songs = Song.objects.all()
    albums = Album.objects.all()

    context ={
        'hesohal':hesohalObj,
        'songs':songs,
        'albums':albums
    }
    return render(request,'musicbeats/single-hesohal.html',context)


def singeTrack(request,pk):
    songObj= Song.objects.get(id=pk)
    singers = Singer.objects.all()
    albums= Album.objects.all()

    context = {
        'song':songObj,
        'singers':singers,
        'albums':albums,
    }

    return render(request,'musicbeats/single-tak-music.html',context)

def singleAlbum(request,pk):
    albumObj= Album.objects.get(id=pk)
    singers = Singer.objects.all()
    albums= Album.objects.all()
    songs = Song.objects.all()

    context = {
        'album':albumObj,
        'singers':singers,
        'albums':albums,
        'songs':songs,
    }
    return render(request,'musicbeats/single-album.html',context)


def albums(request):
    albums , search_query = searchSinger(request)
    custom_range , albums = paginationTheSingers(request,albums,1)
    context = {'albums':albums , 'search_query':search_query,'custom_range':custom_range}

    return render(request,'musicbeats/archive-album.html',context)


@login_required(login_url='login')
def createPlaylist(request):
    profile = request.user.profile
    form = playlistForm()

    if request.method == 'POST':
        form = playlistForm(request.POST)
        if form.is_valid():
            plalist = form.save(commit=False)
            plalist.owner = profile
            plalist.save()
            return redirect('account')

    form = playlistForm
    context = {'form':form}
    return render(request,'musicbeats/')
