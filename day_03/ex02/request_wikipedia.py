#!/usr/local/bin/python3

import dewiki
import requests
import sys


def wiki_request(arg: str):
    r = requests.get("https://en.wikipedia.org/w/api.php",
        params={'action': 'parse',
                'format': 'json',
                'page': arg,
                'prop': 'wikitext',
                'redirects': True}).json()
    if r.get("error") is not None:
        raise Exception(r["error"]["info"])
    return dewiki.from_string(r["parse"]["wikitext"]["*"]).strip()


def main():
    if len(sys.argv) != 2:
        return print("Argument error: enter your request <str>")
    try:
        data = wiki_request(sys.argv[1])
        f = open("{name}.wiki".format(name=sys.argv[1]), "w")
        f.write(data)
        f.close()
    except Exception as e:
        return print(e)


if __name__ == '__main__':
    main()
