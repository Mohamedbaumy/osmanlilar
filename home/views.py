from django.shortcuts import render
from .models import Movie,Episode,Link
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.



# Home Page
def home(request):
    # All Movies
    movies = Movie.objects.all()
    # All Episodes
    object_list = Episode.objects.all()
    paginator = Paginator(object_list,30)
    page = request.GET.get('page')
    try:
        tv = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        tv = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        tv = paginator.page(paginator.num_pages)
    context = {
        'movies':movies[:12],
        'tv':tv,
        'page':page,
        
    }
    return render(request, 'home.html', context)

# Series List and Movie Detail
def movie_list(request,slug):
    # get Movie by slug
    movie = Movie.objects.filter(slug=slug)[0]
    # Series List
    if movie.film_type == 'tv':
        # All Episodes
        object_list = movie.episode.all()
        # Pagination
        paginator = Paginator(object_list,30)
        page = request.GET.get('page')
        try:
            episodes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            episodes = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            episodes = paginator.page(paginator.num_pages)
        context = {
            'movie':movie,
            'episodes':episodes,
            'page':page,
        }
        return render(request,'episodes_list.html',context)
    # Movie Detail
    else:
        movie.views += 1
        movie.save()
        # Get First server 
        watch_server = movie.movie_links.all()[0]
        # All Movie
        movies = Movie.objects.all().exclude(film_type='tv')[0:9]
        # All Series
        series = Movie.objects.all().exclude(film_type='movie')[0:9]
        context = {
            'movie':movie,
            'watch_server':watch_server,
            'movies':movies,
            'series':series
        }
        return render(request,'film_detail.html',context)

# Episode Detail
def episode_detail(request,slug):
    # Get Episode by slug
    episode = Episode.objects.filter(slug=slug)[0]
    episode.views += 1
    episode.save()
    # Get First server 
    watch_server = episode.episode_links.all()[0]
    
    # All Series Episodes
    ser_epi = episode.movie.episode.all()[0:9]
    # All Movies
    movies = Movie.objects.all().exclude(id=episode.movie.id)[0:9]
    
    context = {
        'episode':episode,
        'watch_server':watch_server,
        'series':ser_epi,
        'movies':movies
    }
    return render(request,'episode_detail.html',context)

# Watch Server
def watch(request,slug):
    # Get First Server
    watched = Link.objects.filter(slug=slug)[0]
    # Movie
    if watched.movie:
        servers = watched.movie.movie_links.all()
        movie = watched.movie
        image = watched.movie.image
    # Series
    else:
        servers = watched.episode.episode_links.all()
        movie = watched.episode
        image = watched.episode.movie.image
    
    context = {
            'watched':watched,
            'servers':servers,
            'movie':movie,
            'image':image
    }
    return render(request,'show_server.html',context)

# Movies
def movies(request):
    # All Movies
    object_list = Movie.objects.all().exclude(film_type='tv')
    # Pagination
    paginator = Paginator(object_list,30)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        movies = paginator.page(paginator.num_pages)
    context = {
        'movies':movies,
        'page':page,
    }
    return render(request,'movie_list.html', context)

# Series
def series(request):
    # All Series
    object_list = Movie.objects.all().exclude(film_type='movie')
    # Pagination
    paginator = Paginator(object_list,30)
    page = request.GET.get('page')
    try:
        series = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        series = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        series = paginator.page(paginator.num_pages)
    context = {
        'series':series,
        'page':page,
    }
    return render(request,'series_list.html', context)


def search(request):
    query = request.GET.get('q')
    object_list = Movie.objects.filter(Q(title__icontains=query) | Q(caption__icontains=query))
    # Pagination
    paginator = Paginator(object_list,30)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        movies = paginator.page(paginator.num_pages)
    context = {
        'movies':movies,
        'page':page,
    }
    return render(request,'search_list.html', context)


    