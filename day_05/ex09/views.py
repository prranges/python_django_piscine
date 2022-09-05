from django.http import HttpResponse
from django.shortcuts import render
from .models import People


def display(request):
    try:
        datas = People.objects.filter(homeworld__climate__contains='windy')\
            .values('name', 'homeworld__name', 'homeworld__climate')\
            .order_by('name')
        if len(datas) == 0:
            raise People.DoesNotExist
        return render(request, 'ex09/display.html', {"datas": datas})
    except People.DoesNotExist as e:
        return HttpResponse("No data available")