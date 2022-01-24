from django.urls import path
from . import views

urlpatterns = [
    path('playlist/', views.playLists, name="playlist"),
    path('singers/',views.singers,name="singers"),
    path('singer/<str:pk>/',views.singer,name='singer'),
    path('player/<str:pk>/',views.play,name="play"),
    path('single-hesohal/<str:pk>/',views.single_hesohal,name="single-hesohal"),
    path('single-track/<str:pk>/',views.singeTrack,name="single-track"),
    path('single-album/<str:pk>/',views.singleAlbum,name="single-album"),
]