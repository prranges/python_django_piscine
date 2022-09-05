from django import db
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import RemoveForm, UpdateForm

MOVIES = [
    {
        "episode_nb": 1,
        "title": "The Phantom Menace",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "1999-05-19"
    },
    {
        "episode_nb": 2,
        "title": "Attack of the Clones",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2002-05-16"
    },
    {
        "episode_nb": 3,
        "title": "Revenge of the Sith",
        "director": "George Lucas",
        "producer": "Rick McCallum",
        "release_date": "2005-05-19"
    },
    {
        "episode_nb": 4,
        "title": "A New Hope",
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1977-05-25"
    },
    {
        "episode_nb": 5,
        "title": "The Empire Strikes Back",
        "director": "Irvin Kershner",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1980-05-17"
    },
    {
        "episode_nb": 6,
        "title": "Return of the Jedi",
        "director": "Richard Marquand",
        "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
        "release_date": "1983-05-25"
    },
    {
        "episode_nb": 7,
        "title": "The Force Awakens",
        "director": "J. J. Abrams",
        "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
        "release_date": "2015-12-11"
    }
]


def populate(request):
    status = []
    for movie in MOVIES:
        try:
            Movies.objects.create(
                title=movie['title'],
                episode_nb=movie['episode_nb'],
                director=movie['director'],
                producer=movie['producer'],
                release_date=movie['release_date'],
            )
            status.append("OK")
        except db.Error as e:
            status.append(e)
    return HttpResponse("<br/>".join(str(i) for i in status))


def display(request):
    try:
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Movies.DoesNotExist
        return render(request, 'ex07/display.html', {"movies": movies})
    except Movies.DoesNotExist as e:
        return HttpResponse("No data available")


def remove(request):
    try:
        if request.method == 'POST':
            try:
                movies = Movies.objects.all()
                if len(movies) == 0:
                    raise Movies.DoesNotExist
            except Movies.DoesNotExist as e:
                return redirect(request.path)
            choices = ((movie.title, movie.title) for movie in movies)
            data = RemoveForm(choices, request.POST)
            if data.is_valid():
                try:
                    Movies.objects.get(title=data.cleaned_data['title']).delete()
                except db.Error as e:
                    print(e)
            return redirect(request.path)
        elif request.method == 'GET':
            try:
                movies = Movies.objects.all()
                if len(movies) == 0:
                    raise Movies.DoesNotExist
            except Movies.DoesNotExist as e:
                print(e)
                return HttpResponse("No data available")
            choices = ((movie.title, movie.title) for movie in movies)
            context = {"form": RemoveForm(choices)}
            return render(request, 'ex07/remove.html', context)
    except Exception as e:
        print(e)


def update(request):
    try:
        if request.method == 'POST':
            try:
                movies = Movies.objects.all()
                if len(movies) == 0:
                    raise Movies.DoesNotExist
            except Movies.DoesNotExist as e:
                return redirect(request.path)
            choices = ((movie.title, movie.title) for movie in movies)
            data = UpdateForm(choices, request.POST)
            if data.is_valid():
                try:
                    movie = Movies.objects.get(title=data.cleaned_data['title'])
                    movie.opening_crawl = data.cleaned_data['opening_crawl']
                    movie.save()
                except db.Error as e:
                    print(e)
            return redirect(request.path)
        elif request.method == 'GET':
            try:
                movies = Movies.objects.all()
                if len(movies) == 0:
                    raise Movies.DoesNotExist
            except Movies.DoesNotExist as e:
                print(e)
                return HttpResponse("No data available")
            choices = ((movie.title, movie.title) for movie in movies)
            context = {"form": UpdateForm(choices)}
            return render(request, 'ex07/update.html', context)
    except Exception as e:
        print(e)