from django.http import HttpResponse
from django.conf import settings
import psycopg2
from django.shortcuts import render

TABLE_PLANETS = 'ex08_planets'
TABLE_PEOPLE = 'ex08_people'
SQL_CREATE_TABLES = """
    CREATE TABLE {planets} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        climate VARCHAR,
        diameter integer,
        orbital_period integer,
        population bigint,
        rotation_period integer,
        surface_water REAL,
        terrain VARCHAR(128));
        
    CREATE TABLE {people} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        birth_year VARCHAR(32),
        gender VARCHAR(32),
        eye_color VARCHAR(32),
        hair_color VARCHAR(32),
        height integer,
        mass REAL,
        homeworld VARCHAR(64) REFERENCES {planets}(name));
        """.format(planets=TABLE_PLANETS, people=TABLE_PEOPLE)
SQL_INSERT_PLANETS = """
        INSERT INTO {planets} (
            name,
            climate,
            diameter,
            orbital_period,
            population,
            rotation_period,
            surface_water,
            terrain)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """.format(planets=TABLE_PLANETS)
SQL_INSERT_PEOPLE = """
        INSERT INTO {people} (
            name,
            birth_year,
            gender,
            eye_color,
            hair_color,
            height,
            mass,
            homeworld)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """.format(people=TABLE_PEOPLE)
SQL_SELECT_TABLE = """
        SELECT
            {people}.name,
            {people}.homeworld,
            {planets}.climate
        FROM
            {planets}
            RIGHT JOIN {people}
            ON
                {people}.homeworld = {planets}.name
                where
                    {planets}.climate
                    LIKE '%windy%'
            ORDER BY {planets}.name;
        """.format(people=TABLE_PEOPLE, planets=TABLE_PLANETS)


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
            c.execute(SQL_CREATE_TABLES)
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
            try:
                with open('ex08/data/planets.csv', 'r') as f_planets:
                    c.copy_from(f_planets, 'ex08_planets', null='NULL', columns=['name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'])
                status.append("OK")
                connection.commit()
            except Exception as e:
                connection.rollback()
                status.append(e)
            try:
                with open('ex08/data/people.csv', 'r') as f_people:
                    c.copy_from(f_people, 'ex08_people', null='NULL', columns=['name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'])
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
            datas = c.fetchall()
        return render(request, 'ex08/display.html', {"datas": datas})
    except Exception as e:
        return HttpResponse("No data available")
    finally:
        connection.close()