from django.http import HttpResponse
from django.conf import settings
import psycopg2

TABLE_NAME = 'ex00_movies'
SQL_CREATE_TABLE = """
    CREATE TABLE {table_name} (
        title VARCHAR(64) UNIQUE NOT NULL,
        episode_nb integer PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL);
        """.format(table_name=TABLE_NAME)

def init(request):
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password= settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )
        with connection.cursor() as c:
            c.execute(SQL_CREATE_TABLE)
            connection.commit()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)
