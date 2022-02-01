from django.urls import path
from . import views

urlpatterns = [
    path('singers/',views.singers,name="singers"),
    path('singer/<str:pk>/',views.singer,name='singer'),
    path('player/<str:pk>/',views.play,name="play"),
    path('single-hesohal/<str:pk>/',views.single_hesohal,name="single-hesohal"),
    path('single-track/<str:pk>/',views.singeTrack,name="single-track"),
    path('single-album/<str:pk>/',views.singleAlbum,name="single-album"),
    path('albums/',views.albums,name = "albums"),
    path('archive-hesohal/',views.hesohals,name="hesohals"),
    path('archive-singeTrack/',views.singleSongs,name="singleTracks"),
    path('search-songs/',views.searchSongs , name = "search-songs"),
    path('archive-playlist/',views.adminPlaylists,name="admin-playlists"),
    path('single-playlist<str:pk>/', views.adminPlaylist, name="single-admin-playlist"),
]