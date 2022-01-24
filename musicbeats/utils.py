from django.db.models import Q
from .models import Tag , Song
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger


def paginationTheSinger(request,singers,results):
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


def searchSingers(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    songs= Song.objects.distinct().filter(
        Q(name__icontains=search_query) 



    )

