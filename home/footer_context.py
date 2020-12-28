from .models import Movie,Adds

def footer(request):
    footers = Movie.objects.filter(film_type='tv')
    return {'footers':footers}

def adds(request):
    adds = Adds.objects.filter(active=True)
    return {'adds':adds}