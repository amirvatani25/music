from django.db.models import Q
from .models import Tag , Song ,Singer , Album , Hesohal
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

#songs and main pagination and search
def paginationTheSongs(request,songs,results):
    page = request.GET.get('page')
    paginator = Paginator(songs,results)
    try:
        songs=paginator.page(page)
    except PageNotAnInteger:
        page = 1
        songs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        songs = paginator.page(page)


    leftpages = (int(page)-4)

    if leftpages<1:
        leftpages=1

    rightpages= (int(page)+5)

    if rightpages>paginator.num_pages:
        rightpages=paginator.num_pages+1

    custom_range= range(leftpages,rightpages)

    return custom_range,songs


def searchSongs(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    songs= Song.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(singer__name__icontains=search_query )|
        Q(album__name__icontains=search_query)|
        Q(tags__in=tags)


    )
    return songs , search_query


#singer pagination and search
def paginationTheSingers(request,singers,results):
    page = request.GET.get('page')
    paginator = Paginator(singers,results)
    try:
        singers=paginator.page(page)
    except PageNotAnInteger:
        page = 1
        singers = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        singers = paginator.page(page)


    leftpages = (int(page)-4)

    if leftpages<1:
        leftpages=1

    rightpages= (int(page)+5)

    if rightpages>paginator.num_pages:
        rightpages=paginator.num_pages+1

    custom_range= range(leftpages,rightpages)

    return custom_range,singers


def searchSinger(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    singers= Singer.objects.distinct().filter(
        Q(name__icontains=search_query)


    )
    return singers , search_query

#album pagination and search
def paginationTheAlbum(request,albums,results):
    page = request.GET.get('page')
    paginator = Paginator(albums,results)
    try:
        albums=paginator.page(page)
    except PageNotAnInteger:
        page = 1
        albums = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        albums = paginator.page(page)


    leftpages = (int(page)-4)

    if leftpages<1:
        leftpages=1

    rightpages= (int(page)+5)

    if rightpages>paginator.num_pages:
        rightpages=paginator.num_pages+1

    custom_range= range(leftpages,rightpages)

    return custom_range,albums


def searchAlbum(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    albums= Album.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(singer__name__icontains=search_query )|
        Q(tags__in=tags)
    )
    return albums , search_query


#search and pagination of hesohal

def paginationTheHesohal(request,hesohals,results):
    page = request.GET.get('page')
    paginator = Paginator(hesohals,results)
    try:
        hesohals=paginator.page(page)
    except PageNotAnInteger:
        page = 1
        hesohals = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        hesohals = paginator.page(page)


    leftpages = (int(page)-4)

    if leftpages<1:
        leftpages=1

    rightpages= (int(page)+5)

    if rightpages>paginator.num_pages:
        rightpages=paginator.num_pages+1

    custom_range= range(leftpages,rightpages)

    return custom_range,hesohals


def searchHesohal(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    hesohals= Album.objects.distinct().filter(
        Q(name__icontains=search_query)
    )
    return hesohals , search_query




