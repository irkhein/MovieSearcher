from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'Movies/index.html', {'all_movies': all_movies })


def movie(request, item_id):
    # try:
    #    movie_item = Movie.objects.get(id=item_id)
    # except Movie.DoesNotExist:
    #    raise Http404("Movie does not exist")
    movie_item = get_object_or_404(Movie, id=item_id)
    return render(request, 'Movies/movie.html', {'movie': movie_item, 'rate': movie_item.rate()})


def like(request, item_id):
    # try:
    #    movie_item = Movie.objects.get(id=item_id)
    # except Movie.DoesNotExist:
    #    raise Http404("Movie does not exist")
    movie_item = get_object_or_404(Movie, id=item_id)
    movie_item.like += 1
    movie_item.save()
    return render(request, 'Movies/movie.html', {'movie': movie_item, 'rate': movie_item.rate()})