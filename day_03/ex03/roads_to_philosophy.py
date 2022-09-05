#!/usr/local/bin/python3

import sys
import requests
from bs4 import BeautifulSoup


def get_new_request(request):
    r = requests.get('https://en.wikipedia.org/wiki/' + request)
    if r.status_code != 200:
        print('It leads to a dead end!') if r.status_code == 404 else print('HTTP error ', str(r.status_code))
        exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        new_request = soup.select('p > a')
        for a in new_request:
            if not a.attrs.get('href').startswith('/wiki/Help:') \
                    and not a.attrs.get('href').startswith('/wiki/File:') \
                    and not a.attrs.get('href').startswith('/wiki/Russian_language'):
                return a.attrs.get('title')
    except Exception as e:
        raise SystemExit('It leads to a dead end!')


def wiki_request(request):
    roads = [request]
    while request != 'philosophy':
        if request is not None:
            print(request.capitalize())
        request = get_new_request(request)
        if request in roads:
            print('It leads to an infinite loop!')
            exit(1)
        roads.append(request)
    return roads


def main():
    if len(sys.argv) != 2:
        return print("Argument error: enter your request <str>")
    try:
        roads = wiki_request(sys.argv[1].lower())
        print(str(len(roads)) + " road(s) from " + roads[0] + " to philosophy!")
    except Exception as e:
        raise SystemExit('It leads to a dead end!')


if __name__ == '__main__':
    main()
