from django.http import HttpResponse
from django.conf import settings
import psycopg2
from django.shortcuts import render, redirect
from .forms import RemoveForm

TABLE_NAME = 'ex04_movies'
SQL_CREATE_TABLE = """
    CREATE TABLE {table_name} (
        title VARCHAR(64) UNIQUE NOT NULL,
        episode_nb integer PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL);
        """.format(table_name=TABLE_NAME)
SQL_INSERT_DATA = """
        INSERT INTO {table_name} (
            title,
            episode_nb,
            director,
            producer,
            release_date)
        VALUES (%s, %s, %s, %s, %s);
        """.format(table_name=TABLE_NAME)
SQL_SELECT_TABLE = """
        SELECT * FROM {table_name};
        """.format(table_name=TABLE_NAME)
SQL_SELECT_TITLE = """
        SELECT title FROM {table_name};
        """.format(table_name=TABLE_NAME)
SQL_DELETE_TITLE = """
        DELETE FROM {table_name} WHERE title = %s
        """.format(table_name=TABLE_NAME)
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


def get_connection():
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],

        )
        return connection
    except Exception as e:
        print(e)


def init(request):
    try:
        connection = get_connection()
        with connection.cursor() as c:
            c.execute(SQL_CREATE_TABLE)
            connection.commit()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)
    finally:
        connection.close()


def populate(request):
    try:
        connection = get_connection()
        status = []
        with connection.cursor() as c:
            for movie in MOVIES:
                try:
                    c.execute(SQL_INSERT_DATA, [
                        movie['title'],
                        movie['episode_nb'],
                        movie['director'],
                        movie['producer'],
                        movie['release_date'],
                    ])
                    status.append("OK")
                    connection.commit()
                except Exception as e:
                    connection.rollback()
                    status.append(e)
        return HttpResponse("<br/>".join(str(i) for i in status))
    except Exception as e:
        return HttpResponse(e)
    finally:
        connection.close()


def display(request):
    try:
        connection = get_connection()
        with connection.cursor() as c:
            c.execute(SQL_SELECT_TABLE)
            movies = c.fetchall()
        return render(request, 'ex04/display.html', {"movies": movies})
    except Exception as e:
        return HttpResponse("No data available")
    finally:
        connection.close()


def remove(request):
    try:
        connection = get_connection()
        if request.method == 'POST':
            try:
                with connection.cursor() as c:
                    c.execute(SQL_SELECT_TITLE)
                    movies = c.fetchall()
                choices = ((movie[0], movie[0]) for movie in movies)
            except Exception as e:
                print(e)
            data = RemoveForm(choices, request.POST)
            if data.is_valid():
                try:
                    with connection.cursor() as c:
                        c.execute(SQL_DELETE_TITLE, [data.cleaned_data['title']])
                    connection.commit()
                except Exception as e:
                    print(e)
            return redirect(request.path)
        elif request.method == 'GET':
            try:
                with connection.cursor() as c:
                    c.execute(SQL_SELECT_TABLE)
                    movies = c.fetchall()
                    if not movies:
                        return HttpResponse("No data available")
                context = {'form': RemoveForm(choices=((movie[0], movie[0]) for movie in movies))}
                return render(request, 'ex04/remove.html', context)
            except Exception as e:
                print(e)
        return HttpResponse("No data available")
    except Exception as e:
        print(e)