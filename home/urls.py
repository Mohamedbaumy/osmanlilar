from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('movie/<slug:slug>/', views.movie_list,name='movie_detail'),
    path("episode/<slug>/",views.episode_detail, name="episode_detail"),
    path("show/<slug>/",views.watch, name="show"),
    path("movies/",views.movies, name="movies"),
    path("series/",views.series, name="series"),
    path("search/",views.search, name="search"),
]
