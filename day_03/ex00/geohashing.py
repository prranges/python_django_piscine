#!/usr/local/bin/python3

import antigravity
import sys


def main():
    try:
        assert (len(sys.argv) == 4), "3 args needed"
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3].encode('utf-8')
        antigravity.geohash(latitude, longitude, date)
    except Exception as e:
        print("Error:", e, "\nUsage: python3 geohashing.py latitude<long> longitude<long> date<str>")


if __name__ == '__main__':
    main()
